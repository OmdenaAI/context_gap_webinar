import pytest

from wallet.task1_daily_limit.contextual import (
    TransferServiceContextual,
)
from wallet.errors import DailyLimitExceededError


class FakeLedgerRepository:
    def __init__(self, total_today: float):
        self.total_today = total_today

    def get_total_transferred_today(self, user_id: int) -> float:
        return self.total_today


def test_transfer_within_cumulative_limit():
    repo = FakeLedgerRepository(total_today=4000)
    service = TransferServiceContextual(
        daily_limit=10000,
        ledger_repository=repo,
    )

    result = service.process_transfer(
        user_id=1,
        amount=3000,
    )

    assert result is True


def test_transfer_exceeds_cumulative_limit():
    repo = FakeLedgerRepository(total_today=9000)
    service = TransferServiceContextual(
        daily_limit=10000,
        ledger_repository=repo,
    )

    with pytest.raises(DailyLimitExceededError):
        service.process_transfer(
            user_id=1,
            amount=2000,
        )

