from Datetime.custom_datetime import CustomDatetime
import pytest

def test_default_creation():
    custom_datetime = CustomDatetime()
    assert isinstance(custom_datetime, CustomDatetime)

def test_iso_formatting():
    custom_datetime = CustomDatetime(2023, 11, 11, 12, 30, 45)
    assert custom_datetime.format_iso() == "2023-11-11T12:30:45"

def test_human_readable_formatting():
    custom_datetime = CustomDatetime(2023, 11, 11, 12, 30, 45)
    assert custom_datetime.format_human_readable() == "2023-11-11 12:30:45"

def test_date_validation():
    assert CustomDatetime.validate_date(2023, 11, 11)
    assert not CustomDatetime.validate_date(2023, 13, 32)

def test_date_difference():
    custom_datetime1 = CustomDatetime(2023, 11, 11)
    custom_datetime2 = CustomDatetime(2023, 11, 1)
    assert CustomDatetime.date_difference(custom_datetime1, custom_datetime2) == (10, 1, 0)

def test_date_from_string():
    date_str = "2023-11-11T12:30:45"
    custom_datetime = CustomDatetime.date_from_string(date_str)
    assert custom_datetime.format_human_readable() == "2023-11-11 12:30:45"

def test_weekday_calculation():
    custom_datetime = CustomDatetime(2023, 11, 11)
    assert custom_datetime.weekday_calculation() == "Saturday"

# Additional tests for error handling

def test_invalid_date_creation():
    with pytest.raises(ValueError):
        CustomDatetime(year=2023, month=13, day=32)

def test_invalid_date_from_string():
    with pytest.raises(ValueError):
        CustomDatetime.date_from_string("2023-13-32T12:30:45")
