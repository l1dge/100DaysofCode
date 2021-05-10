import itertools as it


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    res = []

    for count, num in enumerate(sequence, start=1):
        if count == 1:
            prev = num
            res = [round(num, 2)]
        else:
            ans = (num + prev) / count
            res.append(round(ans, 2))
            prev = prev + num

    return res


running_mean([])