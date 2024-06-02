def myfunc(*args):
    result = []
    for num in args:
        if num % 2 == 0:
            result.append(num)
    return result