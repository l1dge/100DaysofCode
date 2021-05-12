from enum import Enum
import pytest


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
    Use the values in the Equality Enum:
    - return SAME_REFERENCE if both lists reference the same object
    - return SAME_ORDERED if they have the same content and order
    - return SAME_UNORDERED if they have the same content unordered
    - return SAME_UNORDERED_DEDUPED if they have the same unordered content
      and reduced to unique items
    - return NO_EQUALITY if none of the previous cases match"""

    if id(list1) == id(list2):
        return Equality.SAME_REFERENCE
    elif list1 == list2:
        return Equality.SAME_ORDERED
    elif list1 != list2:
        list1.sort()
        list2.sort()
        if list1 == list2:
            return Equality.SAME_UNORDERED
        elif list1 != list2:
            list1 = list(dict.fromkeys(list1))
            list2 = list(dict.fromkeys(list2))
            list1.sort()
            list2.sort()
            if list1 == list2:
                return Equality.SAME_UNORDERED_DEDUPED
            elif list1 != list2:
                return Equality.NO_EQUALITY


# Tests
def test_same_reference():
    a = [1, 2, 3, 4]
    b = a
    # shallow copy (do not change original), alternatively use the copy module
    c = a[:]
    assert check_equality(a, b) == Equality.SAME_REFERENCE
    assert check_equality(a, c) != Equality.SAME_REFERENCE


def test_same_ordered():
    a = [1, 2, 3, 4]
    b = a[:]
    c = a
    assert check_equality(a, b) == Equality.SAME_ORDERED
    assert check_equality(a, c) != Equality.SAME_ORDERED  # SAME_REFERENCE


def test_same_unordered():
    a = [1, 2, 3, 4]
    b = a[::-1]
    c = b[:] + [5]
    assert check_equality(a, b) == Equality.SAME_UNORDERED
    assert check_equality(a, c) != Equality.SAME_UNORDERED


def test_same_unordered_deduped():
    a = [1, 2, 2, 3, 4]
    b = a[:] + [1, 3, 4, 4]
    c = b[:] + [5]
    assert check_equality(a, b) == Equality.SAME_UNORDERED_DEDUPED
    assert check_equality(a, c) != Equality.SAME_UNORDERED_DEDUPED


def test_not_same():
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert check_equality(a, b) == Equality.NO_EQUALITY
