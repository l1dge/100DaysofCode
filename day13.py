import string
import secrets
import pytest, re


def gen_key(parts=4, chars_per_part=8):
    keys = string.ascii_uppercase + string.digits
    codes = ""
    serial = ""
    codes = [
        "".join(secrets.choice(keys) for i in range(chars_per_part))
        for code in range(parts)
    ]

    for key in codes:
        serial += key + "-"
    return serial.rstrip("-")


default_key = re.compile(r"^([A-Z0-9]{8}-){3}[A-Z0-9]{8}$")
shorter_key = re.compile(r"^([A-Z0-9]{4}-){2}[A-Z0-9]{4}$")
longer_key = re.compile(r"^([A-Z0-9]{10}-){9}[A-Z0-9]{10}$")


def test_gen_default_key():
    assert default_key.match(gen_key())


def test_gen_shorter_key():
    assert shorter_key.match(gen_key(parts=3, chars_per_part=4))


def test_gen_longer_key():
    assert longer_key.match(gen_key(parts=10, chars_per_part=10))


gen_key()
test_gen_default_key()
test_gen_shorter_key()
test_gen_longer_key()