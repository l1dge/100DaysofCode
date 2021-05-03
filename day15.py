def fizzbuzz(num):
    res = (
        str("Fizz Buzz")
        if num % 3 == 0 and num % 5 == 0
        else str("Fizz")
        if num % 3 == 0
        else str("Buzz")
        if num % 5 == 0
        else int(num)
    )

    return res


for i in range(1, 15):
    print(fizzbuzz(i))