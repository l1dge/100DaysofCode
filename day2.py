STRING = "bob and julian love pybites!"
STRING2 = "hello"
STRING3 = "pybites loves julian and bob!"
STRING4 = "julian and bob!"

string = STRING2


def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    tmp = string[n:] + string[0:n]

    return tmp


print(rotate(STRING4, 100))
