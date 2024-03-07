# first example
print('first example')
shopping_list = ["milk", "bread", "flower"]
for item in shopping_list:
    print(item)

# second example
print('second example')
text = "vision academy tutorials"
count = 0
for item in text:
    if item == 'a':
        count += 1

print(count)

# third example
print('third example')
for i in range(1, 10, 2):
    print(i)

# fourth example
print('fourth')

def compute_power(base, power):
    result = 1
    for i in range(power):
        result *= base

    return result

base = int(input("Please insert the base: "))
power = int(input("Please insert the power: "))
print(compute_power(base, power))