answer = input("Player 1: Please insert the number (1 - 100): ")
answer = int(answer)

is_correct = False
try_count = 0

while try_count < 10 and is_correct == False:
    guess = int(input("Player 2: Please guess a number: "))
    if guess == answer:
        print("Player 2: You Won!")
        is_correct = True
    elif guess > answer:
        print("Your guess is greater than the answer.")
        try_count += 1
    else:
        print("Your guess is smaller than the answer.")
        try_count += 1

if is_correct == False:
    print("Player 2: You Lost!")