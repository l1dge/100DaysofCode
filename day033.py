from collections import Counter

import requests
import pytest

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    carCount = Counter()
    cars = [yr.get("automaker") for yr in data if yr.get("year") == year]
    carCount.update(cars)
    return carCount.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    cars = set(
        (yr.get("model"))
        for yr in data
        if yr.get("year") == year and yr.get("automaker") == automaker
    )
    return cars


# Tests
def test_most_prolific_automaker_1999():
    assert most_prolific_automaker(1999) == "Dodge"


def test_most_prolific_automaker_2008():
    assert most_prolific_automaker(2008) == "Toyota"


def test_most_prolific_automaker_2013():
    assert most_prolific_automaker(2013) == "Hyundai"


def test_get_models_volkswagen():
    models = get_models("Volkswagen", 2008)
    # sets are unordered
    assert len(models) == 2
    assert "Jetta" in models
    assert "Rabbit" in models


def test_get_models_nissan():
    assert get_models("Nissan", 2000) == {"Pathfinder"}


def test_get_models_open():
    # not in data set
    assert get_models("Opel", 2008) == set()


def test_get_models_mercedes():
    models = get_models("Mercedes-Benz", 2007)
    assert len(models) == 3
    assert "SL-Class" in models
    assert "GL-Class" in models
    assert "CL-Class" in models
