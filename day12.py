import pytest


def get_profile(**kwargs):
    reqd = ["name", "profession"]
    name = "julian"
    profession = "programmer"

    if len(kwargs) == 0:
        return name + " is a " + profession
    elif len(kwargs) == 1:
        if not any(i in kwargs for i in reqd):
            raise TypeError()
        else:
            name = kwargs.get("name")
            return name + " is a " + profession
    elif len(kwargs) == 2:
        if not all(i in kwargs for i in reqd):
            raise TypeError()
        else:
            name = kwargs.get("name")
            profession = kwargs.get("profession")
            return name + " is a " + profession
    elif len(kwargs) > 2:
        raise TypeError()


def test_no_arguments():
    assert get_profile() == "julian is a programmer"


def test_one_positional_arg():
    with pytest.raises(TypeError):
        get_profile("julian")


def test_wrong_single_kw():
    with pytest.raises(TypeError):
        get_profile(test=True)


def test_wrong_additional_kw():
    with pytest.raises(TypeError):
        get_profile(name="bob", profession="software developer", another_flag=False)


def test_correct_kw_second_default():
    assert get_profile(name="bob") == "bob is a programmer"


def test_two_correct_kws():
    ret = get_profile(name="bob", profession="software developer")
    assert ret == "bob is a software developer"


print(test_no_arguments())
print(test_one_positional_arg())
print(test_wrong_single_kw())
print(test_wrong_additional_kw())
print(test_correct_kw_second_default())
print(test_two_correct_kws())