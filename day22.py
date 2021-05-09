import re
import pytest


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    word = re.sub(r"[^A-Za-z0-9 ]+", "", input_string)
    return word
    # if type(input_string) == list:
    #     for words in input_string:
    #         words = re.sub(r"[^A-Za-z0-9 ]+", "", words)
    #         return words
    # else:
    #     word = re.sub(r"[^A-Za-z0-9 ]+", "", input_string)
    #     return word


@pytest.mark.parametrize(
    "input_argument, expected_return",
    [
        ("Hello, I am Tim.", "Hello I am Tim"),
        (
            ";String. with. punctuation characters!",
            "String with punctuation characters",
        ),
        ("Watch out!!!", "Watch out"),
        ("Spaces - should - work the same, yes?", "Spaces  should  work the same yes"),
        (
            "Some other (chars) |:-^, let's delete them",
            "Some other chars  lets delete them",
        ),
    ],
)
def test_remove_punctuation(input_argument, expected_return):
    assert remove_punctuation(input_argument) == expected_return
