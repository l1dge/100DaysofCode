from collections import deque
import pytest


def my_queue(n=5):
    res = deque([], maxlen=n)

    return res


if __name__ == "__main__":
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """


q1 = my_queue(5)
q2 = my_queue(3)
q3 = my_queue(7)


@pytest.mark.parametrize(
    "fn_in,expected_result",
    [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 2]),
        (3, [0, 1, 2, 3]),
        (4, [0, 1, 2, 3, 4]),
        (5, [1, 2, 3, 4, 5]),
        (6, [2, 3, 4, 5, 6]),
    ],
)
def test_queue_default_arg(fn_in, expected_result):
    q1.append(fn_in)
    assert list(q1) == expected_result


@pytest.mark.parametrize(
    "fn_in,expected_result",
    [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 2]),
        (3, [1, 2, 3]),
        (4, [2, 3, 4]),
        (5, [3, 4, 5]),
        (6, [4, 5, 6]),
    ],
)
def test_queue_less_items(fn_in, expected_result):
    q2.append(fn_in)
    assert list(q2) == expected_result


@pytest.mark.parametrize(
    "fn_in,expected_result",
    [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 2]),
        (3, [0, 1, 2, 3]),
        (4, [0, 1, 2, 3, 4]),
        (5, [0, 1, 2, 3, 4, 5]),
        (6, [0, 1, 2, 3, 4, 5, 6]),
    ],
)
def test_queue_more_items(fn_in, expected_result):
    q3.append(fn_in)
    assert list(q3) == expected_result


my_queue()
