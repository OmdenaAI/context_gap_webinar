from wallet.errors import DailyLimitExceededError


class TransferServiceContextual:
    def __init__(self, daily_limit: float, ledger_repository):
        self.daily_limit = daily_limit
        self.ledger_repository = ledger_repository

    def process_transfer(self, user_id: int, amount: float) -> bool:
        total_today = self.ledger_repository.get_total_transferred_today(
            user_id
        )

        if total_today + amount > self.daily_limit:
            raise DailyLimitExceededError(
                "Daily cumulative limit exceeded."
            )

        return True
