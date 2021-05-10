import pytest
import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return calendar.day_name[date.weekday()]


def test_leonardo_dicaprio_bday():
    dt = date(1974, 11, 11)
    assert weekday_of_birth_date(dt) == "Monday"


def test_will_smith_bday():
    dt = date(1968, 9, 25)
    assert weekday_of_birth_date(dt) == "Wednesday"


def test_robert_downey_bday():
    dt = date(1965, 4, 4)
    assert weekday_of_birth_date(dt) == "Sunday"
