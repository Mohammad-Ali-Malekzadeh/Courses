num1 = input("Please insert the first number: ")
num2 = input("Please insert the second number: ")
operation = input("Please insert your desired operation: +, -, *, / : ")

if operation == '+':
    result = float(num1) + float(num2)
elif operation == '-':
    result = float(num1) - float(num2)
elif operation == '*':
    result = float(num1) * float(num2)
elif operation == '/':
    result = float(num1) / float(num2)
else:
    result = 'The operation inserted by the user is wrong!'

print(result)