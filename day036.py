import pytest

NOT_FOUND = "Not found"

group1 = {"tim": 30, "bob": 17, "ana": 24}
group2 = {"ana": 26, "thomas": 64, "helen": 26}
group3 = {"brenda": 17, "otto": 44, "thomas": 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
    If name in > 1 dict, return the match of the group with
    greatest N (so group3 > group2 > group1)
    """
    groups = [group1, group2, group3]
    ans = {}
    if not isinstance(name, str):
        return NOT_FOUND
    else:
        nameLC = name.lower()

        for group in groups:
            if nameLC in group.keys():
                ans.update({nameLC: group.get(nameLC)})
            else:
                pass
        if len(ans) == 0:
            return NOT_FOUND
        else:
            return ans.get(nameLC)


# Tests
def test_regular_name():
    assert get_person_age("tim") == 30
    assert get_person_age("helen") == 26
    assert get_person_age("otto") == 44


def test_case_insensitive_lookup():
    assert get_person_age("Tim") == 30
    assert get_person_age("BOB") == 17
    assert get_person_age("BrEnDa") == 17


def test_name_not_found():
    assert get_person_age("timothy") == NOT_FOUND
    assert get_person_age(None) == NOT_FOUND
    assert get_person_age(False) == NOT_FOUND
    assert get_person_age(-1) == NOT_FOUND


def test_duplicate_name():
    assert get_person_age("thomas") == 46
    assert get_person_age("ana") == 26


print(get_person_age("tim"))
