select_ex = "n_" + input("Please Select one of the Exercises (1 - 12): ")


def ex1():
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        print("Your Number is is Odd!")
    else:
        print("Your Number is Even!")


def ex2():
    num = int(input("Please Enter a Number: "))
    while num <= 100:
        print(num)
        num += 1


def ex3():
    numbers = []
    for i in range(0, 3):
        numbers.append(
            int(input("Please Enter your {num} Number: ".format(num=str(i + 1))))
        )

    print(max(numbers))


def ex4():
    num = int(input("Please Enter a Number: "))
    if num < 0:
        print("Please Enter a Positive Number!!!")
        quit()
    result = 0
    for i in range(1, num + 1):
        result += i
    print(result)


def ex5():
    num = int(input("Please Enter a Number: "))
    print(len(str(num)))


def ex6():
    string = input("Please Enter Text: ")
    reversed_str = ""

    for i in range(-1, -(len(string) + 1), -1):
        reversed_str += string[i]

    print(reversed_str)


def ex7():
    string = input("Please Enter Text: ")
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        else:
            lower_count += 1
    print(
        "Your Test have {upper} Upper Case and {lower} Lower Case.".format(
            upper=upper_count, lower=lower_count
        )
    )

exercises = {
    "n_1": ex1,
    "n_2": ex2,
    "n_3": ex3,
    "n_4": ex4,
    "n_5": ex5,
    "n_6": ex6,
    "n_7": ex7,
    # "n_8": ex8,?
    # "n_8": ex9,
    # "n_8": ex10,
    # "n_8": ex11,
    # "n_8": ex12,
}

if not (select_ex in exercises):
    print("Please Enter a Valid input!!!")
    quit()
else:
    exercises[select_ex]()
