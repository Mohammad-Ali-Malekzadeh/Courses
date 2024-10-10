from numpy import random

x = random.randint(1000) #from 0 until parameter.
y = random.rand() # from 0 to 1.
z = random.randint(1000, size=(3,5)) # randomly two dimensioal array.
m = random.choice([3,7,6,5], size=(4,2)) # Selects a number or size given in the input from the list.

print('x:',x)
print('y:',y)
print('z:\n',z)
print('m:\n',m)
