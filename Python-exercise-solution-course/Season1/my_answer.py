select_ex = "n_" + input("Please Select one of the Exercises (1 - 12): ")

def ex1():
    num = int(input('Please enter a number: '))
    if num % 2 == 0:
        print('Your Number is is Odd!')
    else:
        print('Your Number is Even!')

exercises = {
    "n_1": ex1,
    # "n_2": ex2,
    # "n_3": ex3,
    # "n_5": ex5,
    # "n_6": ex6,
    # "n_7": ex7,
    # "n_8": ex8,
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