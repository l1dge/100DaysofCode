import pytest

"""
Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}

# complete :
def check_bt(donor, recipient):
    """Checks red blood cell compatibility based on 8 blood types
    Args:
    donor (int | str | Bloodtype): red blood cell type of the donor
    recipient (int | str | Bloodtype): red blood cell type of the recipient
    Returns:
    bool: True for compatability, False otherwise.
    """
    donor = _check_convert_input(donor)
    recipient = _check_convert_input(recipient)
    d = donor.value
    r = recipient.value
    anti_gen_comp = (r // 4 % 2 - d // 4 % 2, r // 2 % 2 - d // 2 % 2, r % 2 - d % 2)
    return all(agc >= 0 for agc in anti_gen_comp)


def _check_convert_input(inpval):
    """Checks onput data type and value,
    if necessary and possible it converts it to Bloodtype.
    Arg:
    inpval (int | str | Bloodtype)
    Returns:
    (Bloodtype): converted (if needed) impval
    """
    if isinstance(inpval, Bloodtype):
        return inpval
    if isinstance(inpval, int):
        if 0 <= inpval <= 7:
            return Bloodtype(inpval)
        else:
            raise ValueError
    if isinstance(inpval, str):
        if inpval in blood_type_text.keys():
            return blood_type_text[inpval]
        else:
            raise ValueError
    else:
        raise TypeError


# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )


# Tests
def test_universal_donor():
    donor = Bloodtype.ZERO_NEG
    for i in range(8):
        recipient = Bloodtype(i)
        assert check_bt(donor, recipient)


def test_universal_recipient():
    recipient = Bloodtype.AB_POS
    for i in range(8):
        donor = Bloodtype(i)
        assert check_bt(donor, recipient)


def test_AB_POS_can_donate_to_own_group_only_numeric_input():
    donor = 7
    for i in range(7):
        recipient = i
        assert check_bt(donor, recipient) is False


def test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input():
    recipient = 0
    for i in range(1, 8):
        donor = i
        assert check_bt(donor, recipient) is False


def test_red_blood_cell_compatibility():
    assert check_bt(Bloodtype.A_NEG, Bloodtype.A_NEG)  # own
    assert check_bt(Bloodtype.B_NEG, Bloodtype.B_POS)
    assert check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG)


def test_red_blood_cell_incompatibility():
    assert check_bt(Bloodtype.B_POS, Bloodtype.B_NEG) is False
    assert check_bt(Bloodtype.A_NEG, Bloodtype.B_NEG) is False
    assert check_bt(Bloodtype.AB_NEG, Bloodtype.B_POS) is False
    assert check_bt(Bloodtype.B_NEG, Bloodtype.A_POS) is False


def test_red_blood_cell_compatibility_text_input():
    assert check_bt("0+", "A+")
    assert check_bt("0+", "B+")
    assert check_bt("B-", "B+")
    assert check_bt("A-", "AB-")


def test_red_blood_cell_incompatibility_text_input():
    assert check_bt("0+", "A-") is False
    assert check_bt("0+", "B-") is False
    assert check_bt("B-", "0-") is False
    assert check_bt("AB-", "A+") is False


def test_invalid_value_text_input():
    with pytest.raises(ValueError):
        check_bt("X-", "Y+")
    with pytest.raises(ValueError):
        check_bt("0", "A+")


def test_invalid_value_numeric_input():
    with pytest.raises(ValueError):
        check_bt(8, 1)
    with pytest.raises(ValueError):
        check_bt(3, -1)


def test_invalid_type():
    with pytest.raises(TypeError):
        check_bt(1.0, 1)
    with pytest.raises(TypeError):
        check_bt(3, ["AB", "Rh+"])
