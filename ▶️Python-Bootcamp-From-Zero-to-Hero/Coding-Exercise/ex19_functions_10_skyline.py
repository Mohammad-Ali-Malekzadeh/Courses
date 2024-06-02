def myfunc(string):
    result = ''
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i].lower()
    
    return result