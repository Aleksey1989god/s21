#!/usr/bin/env python3

import pytest
from financial import get_financial_data, validate_input


class TestFinancialModule:

    def test_total_revenue_returns_correct_data(self):
        result = get_financial_data("AAPL", "Total Revenue")

        assert isinstance(result, tuple)
        assert result[0] == "Total Revenue"
        assert len(result) > 1

    def test_return_type_is_tuple(self):
        result = get_financial_data("MSFT", "Total Revenue")
        assert isinstance(result, tuple), f"Expected tuple, got {type(result)}"

    def test_invalid_ticker_raises_exception(self):
        with pytest.raises(Exception):
            get_financial_data("INVALID_TICKER_12345", "Total Revenue")

    def test_input_validation(self):
        validate_input("AAPL", "Total Revenue")

        with pytest.raises(ValueError):
            validate_input("", "Total Revenue")

    def test_different_valid_fields(self):
        valid_fields = ["Total Revenue", "Gross Profit", "Operating Income"]

        for field in valid_fields:
            result = get_financial_data("GOOGL", field)
            assert isinstance(result, tuple)
            assert result[0] == field


if __name__ == "__main__":
    pytest.main([__file__, "-v"])