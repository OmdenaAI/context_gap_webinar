from wallet.task1_daily_limit.naive import (
    TransferServiceNaive,
)


def test_transfer_within_limit():
    service = TransferServiceNaive(daily_limit=10000)

    result = service.process_transfer(amount=5000)

    assert result is True


def test_transfer_exceeds_limit():
    service = TransferServiceNaive(daily_limit=10000)

    result = service.process_transfer(amount=15000)

    assert result is False
