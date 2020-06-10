# loop through something 5 times and multiplle 5 time the result

# total = 1
# loop 5 times
# total = total + 5


def factorial(num):
    if num == 0:
        return num
    return num + factorial(num - 1)


print(factorial(5))
