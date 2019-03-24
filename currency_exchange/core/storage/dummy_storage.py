"""
doc string goes here
"""

__all__ = ['DummyStorage']

# Standard library imports.

# Related third party imports.

# Local application/library specific imports.
from .base import BaseStorage


class DummyStorage(BaseStorage):
    def store_currencies(self, currencies):
        pass

    def store_rates(self, exchange_rates):
        pass

    def get_currencies(self, provider_names, currency_codes):
        pass

    def get_rates(self, provider_names, currency_code, to_currencies=None, on_date=None):
        pass
