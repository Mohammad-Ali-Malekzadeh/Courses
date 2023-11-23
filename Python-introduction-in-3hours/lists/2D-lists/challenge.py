""" 
! Challenge Description
    we want to take 3 gridiron width and height, Then calculate The environment of the football area and Compare with FIFA standard. if the gridiron Environment dosen't match with FIFA standard return error to user.
"""


# For convert integers into words
def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return str(n) + suffix


number_of_football_area = int(input("Please insert number of Football Area: "))
environments = []

def football_area(item):
    item_word = ordinal(item + 1)
    width = int(input(f"Please insert {item_word} Football Area Width: "))
    height = int(input(f"Please insert {item_word} Football Area Height: "))

    # Environment
    environment = (width + height) * 2
    if 300 <= environment <= 360:
        environments.append(f'Your {item_word} Football Area: is Standard.')
    else:
        environments.append(f'Your {item_word} Football Area: isn\'t Standard.')
    

    return [width, height]

football_areas = [football_area(item) for item in range(number_of_football_area)]

def result():
    print('Your Areas:')
    for i in football_areas:
        print(i)
    
    print('\nResult of matching your Area\'s with FiFa')
    for i in environments:
        print(i)

result()