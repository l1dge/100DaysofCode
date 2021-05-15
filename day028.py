from urllib.request import urlretrieve

import pytest


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""

    words = open(file_).read()
    noLines = len(open(file_).readlines())
    noWords = len(words.split())
    noChars = len(words)

    res = f"{noLines}\t{noWords}\t{noChars}\t{file_}"

    return res


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))


# Tests
lines = [b"Hello world", b"Keep calm and code in Python", b"Have a nice weekend"]
py_file = "https://bites-data.s3.us-east-2.amazonaws.com/driving.py"


@pytest.mark.parametrize(
    "some_text, expected",
    [
        (lines[0], "1 2 11"),
        (b"\n".join(lines[:2]), "2 8 40"),
        (b"\n".join(lines), "3 12 60"),
    ],
)
def test_wc(some_text, expected, tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(some_text)
    output = wc(f.resolve())
    # replace tabs / multiple spaces by single space
    counts = " ".join(output.split()[:3])
    assert counts == expected
    # file with/without path allowed
    assert f.name in output


def test_wc_on_real_py_file(tmp_path):
    f = tmp_path / "driving.py"
    urlretrieve(py_file, f)
    output = wc(f.resolve())
    counts = " ".join(output.split()[:3])
    # https://twitter.com/pybites/status/1175795375904628736
    expected = "7 29 216"  # not 8!
    assert counts == expected
    assert f.name in output