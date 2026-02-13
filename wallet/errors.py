class DailyLimitExceededError(Exception):
    """Raised when daily transfer limit is exceeded."""


class AccountSuspendedError(Exception):
    """Raised when account is suspended."""


class AccountClosedError(Exception):
    """Raised when account is closed."""
