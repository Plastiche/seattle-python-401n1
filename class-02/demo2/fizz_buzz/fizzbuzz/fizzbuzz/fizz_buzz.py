def fizz_buzz(num):
    """
    Doc String
    """
    if not num % 15:
        return 'FizzBuzz'
    elif not num % 3:
        return 'Fizz'
    elif not num % 5:
        return 'Buzz'
    return num

