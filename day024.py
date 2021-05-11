def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
    cities between the two"""
    return len(list(set(my_cities) - set(other_cities))) + len(
        list(set(other_cities) - set(my_cities))
    )


# Tests
def test_uncommon_part_overlap():
    my_cities = ["Rome", "Paris", "Madrid", "Chicago", "Seville", "Berlin"]
    other_cities = ["Paris", "Boston", "Sydney", "Madrid", "Moscow", "Lima"]
    assert uncommon_cities(my_cities, other_cities) == 8


def test_uncommon_all_same():
    my_cities = ["Rome", "Paris", "Madrid", "Chicago", "Seville", "Berlin"]
    other_cities = ["Rome", "Paris", "Madrid", "Chicago", "Seville", "Berlin"]
    assert uncommon_cities(my_cities, other_cities) == 0


def test_uncommon_all_different():
    my_cities = ["Rome", "Paris", "Madrid"]
    other_cities = ["Chicago", "Seville", "Berlin"]
    assert uncommon_cities(my_cities, other_cities) == 6