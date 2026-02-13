class TransferServiceNaive:
    def __init__(self, daily_limit: float):
        self.daily_limit = daily_limit

    def process_transfer(self, amount: float) -> bool:
        if amount > self.daily_limit:
            return False
        return True
