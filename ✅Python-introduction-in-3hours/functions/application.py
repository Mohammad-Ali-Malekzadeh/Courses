def say_hello(name, age):
    print("Hello " + name + ". You are " + age)

def add_numbers(a,b):
    c = a + b
    return c

first_name = 'Reza'
age = '40'

num1 = 10
num2 = 15
result = add_numbers(num1, num2)


print('==============================')
print(result)
say_hello(first_name, age)
print('==============================')