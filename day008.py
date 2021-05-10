CHARS0 = ["A", "f", ".", "Q", 2]
CHARS1 = [".", "{", " ^", "%", "a"]
CHARS2 = [1, "=", 3, 4, 5, "A", "b", "a", "b", "c"]
CHARS3 = ["=", "=", "", "/", "/", 9, ":", ";", "?", "¡"]
CHARS4 = list(range(1, 9)) + ["}"] + list("abcde")
CHARS5 = [2, ".", ",", "!"]

chars = CHARS5


def get_index_different_char(chars):
    alphaNumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    count = 0
    for letter in chars:
        if str(letter) in alphaNumeric:
            count += 1

    if count >= len(chars) - 1:
        # print("String is mostly alphanemueric")
        for ind, letter in enumerate(chars):
            if str(letter) not in alphaNumeric:
                return ind

    else:
        # print("String is mostly garbage")
        for ind, letter in enumerate(chars):
            if letter and str(letter) in alphaNumeric:
                return ind


print(get_index_different_char(chars))