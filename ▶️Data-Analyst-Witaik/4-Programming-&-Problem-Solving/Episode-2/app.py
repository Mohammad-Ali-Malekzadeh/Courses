#! مرور جلسه قبل - خرید کردن
""" x = 200
item = input('enter the name of item: ')
price = float(input(f'Enter the price of {item}: '))
t = float(input(f'enter {item}:'))
b = price * t
z = x - b
item2 = input('enter the name of item: ')
price2 = float(input(f'Enter the price of {item2}: '))
t2 = float(input(f'enter {item2}:'))
b2 = price2 * t2
if z > b2:
    print(f'you can by item {item2}: ')
else:
    print(f'you can not buy {item2}: ') """

#! گفته میشه بعد ساختمان داده ها for ابتدا
names = ["tina", "mina", "reza", "ali", "sima"]

# print(names[0])
# print(names[1])
# print(names[2])

# for name in names:
#     print(name)

# همانطور که دیدیم کارمون خیلی راحت تر شد
# به تعداد لیست درون حلقه مون تکرار میشه

#! range(start, stop-1, step)
# for i in range(1,100,5): # 1,99
#     print(f'hi {i}')

""" names = []
for i in range(1,4): #1,2,3
    name = input(f'enter your name({i}):')
    names.append(name)  
print(names) """

""" numbers = []
for i in range(1,6):
    num = int(input(f'enter the num({i}): '))
    numbers.append(num)
x = sum(numbers) / len(numbers)
print(x) """

""" add = []
sub = []
for i in range(1, 6):
    ope = input("enter your choice:(1.-,2,+)")
    if ope == "-":
        num1 = int(input("enter the number1:"))
        num2 = int(input("enter the number2:"))
        x = num1 - num2
        sub.append(x)
        print(x)
    elif ope == "+":
        num1 = int(input("enter the number1:"))
        num2 = int(input("enter the number2:"))
        x = num1 + num2
        add.append(x)
        print(x)
    else:
        print('invalid input')
print(add,sub) """

#! for در استرینگ و اجرایی کردن آن با count یادآوری تابع
""" text = 'this is a python class'     
# print(text.count('s'))
count = 0
for item in text:
    if item == 's':
        count += 1
print(count) """

#! break - بشکن
""" names = ["tina", "mina", "alireza", "reza", "ali", "sima"]
for i in names:
    print(i)
    # if i == 'mina':
    #     break
    # if "r" in i:
    #     break
    if len(i) == 4:
        break """

""" x = [0, 1, 12, 8, 9, 7, 6]
for i in x:
    print(i)
    if i%2 == 0:
        break """

#! continue - نادیده بگیر
""" x = [0, 1, 12, 8, 9, 7, 6]
for i in x:
    if i%2 == 0:
        continue
    print(i)
# بنابراین فرد هارو پرینت خواهد کرد
for i in x:
    if not  i%2 == 0:
        continue
    print(i)
# الان فقط زوج ها پرینت میشن """

""" names = ["tina", "mina", "alireza", "reza", "ali", "sima"]
for i in names:
    # if not 'e' in i:
    #     continue
    # print(i)

    # if len(i) == 4:
    #     continue
    # print(i) """

""" count = 0
for i in 'alializadeh':
    count += 1
    if i == 'a' or i == 'i':
        print('letter', count,'is',i, 'not')
        continue
    print('letter', count,'is',i) """

""" username = input('enter a username less than 6 character:')
count = 1
for i in username:
    print('letter', count,'is',i)
    count += 1
    if count > 6:
        print(f'your username {username} is too long')
        break """

#! for in list (one line)
""" names = ["tina", "mina", "alireza", "reza", "ali", "sima"]
# x = [i.upper() for i in names if len(i) == 4]
x = [i.replace('n', 'hh') for i in names if 'n' in i]
print(x) """

#! split() str => list
# براساس چیزی که میخوایم استرینگ رو جدا میکنه و لیست تولید میکنه
""" text = "this is a python class"
print(text.split()) """

# بک اسلش برای پایتون معنی داره بخاطر همین میتونیم 2 تا بزنیم
""" x = 'D:/MA.Malekzadeh/Github/Courses/▶️Data-Analyst-Witaik/4-Programming-&-Problem-Solving/Episode-2/app.py'
print(x.split('/')) """

#! join list => str
# است split برعکس
""" names = ["tina", "mina", "alireza", "reza", "ali", "sima"]
x = '*'.join(names)
print(x) """

#! set, tuple, dict

#! tuple()
""" n = 'ali', 'mina' #('ali', 'mina')
# کد بالا درست است ولی پایتون بصورت تاپل این دو مقدار رو در متغییر ذخیره میکنه
print(n)
print(type(n))
x = 'ali',
# تاپل تک عضوه میشود """

""" names = ("tina", "mina", "alireza")
print(names[2])
print(names[1:2])
# تفاوت تاپل اینکه نمیشه تغییرش داد """

""" names = ("tina", "mina", "alireza")
print(names + ("omid",)) """

# اگر یک عضو تاپل مون داشته باشه باید یدونه کاما بعدش بنویسیم
""" print(('omid',))
print(('omid'))
print(type(('omid',)))
print(type(('omid'))) """
# برای ایجاد یک تاپل تنها با یک آیتم، باید یک کاما بعد از آیتم اضافه کنید، در غیر این صورت پایتون متغیر را به عنوان یک تاپل تشخیص نخواهد داد.

# اگه یه جایی خیلی نیاز شد که تاپل مون رو تغییر بدیم میتونیم با تبدیل سازی این کار رو انجام بدهیم
""" names = ("tina", "mina", "alireza")
names2 = list(names)
names2.sort()
print(names2)
names = tuple(names2)
print(names) """

#! set = {} (تکراری ها حذف میشه و ترتیب وجود نداره و اهمیت نداره)
# چون ترتیب نیست 2 مورد وجود نخواهد داشت - index and slicing
# names = {'tina', 'mina', 'alireza', 'tina', 'ali'}
# print(names)
#! .add()
# names.add('ali') # یه جا اضافه میشه
#! .update()
# names.update({6,7,8,9,10}) # چندین کاراکتر رو میشه اصافه کرد
# names.update([6,7,8,9,10])
# names.update((6,7,8,9,10)) # مهم نیست تاپل، لیست یا ست باشه همشون یه کار انجام میدن
# names.remove('tina')
#! .pop()
# a = names.pop() # رندوم پاک میکنه
# print(a) #با این کار میتونیم مشخص کنیم که کدوم بصورت رندوم حذف میشه
#! .discard()
# names.discard('tina')
#! .clear()
# names.clear()
# نشون میده ؟ چون نمیخواد با دیگشنری اشتباه بگیریمset() ست خالی می شود ولی چرا مثل لیست بعد از پاک کردن علامت {} رو نشون نمیده و به جاش
# del names # کلا میاد حذف میکنه
# print(names)

#! .union() اجتماع
""" x = {1,5,8,7,9,4}
y = {2,5,9,54}
a = x.union(y)
print(a) """

#! ..intersection() اشتراک
""" x = {1,5,8,7,9,4}
y = {2,5,9,54}
a = x.intersection(y) """

#! .difference() تفاضل
""" x = {1,5,8,7,9,4}
y = {2,5,9,54}
a = x.difference(y)
print(a) """

#! Dictionary {key:value}
# تکراری داشته باشیم، همون کلید آپدیت میشه مثل تغییر متغییر key اگر در یک دیگشنری 2 تا
""" user = {
    'name': 'sara',
    'age': 12,
    'test': True,
    'test2': [6,8,9],
    'name': True,
    1: 8888
}
print(user) """

#! .get('key', 'it prints this argument as a message if the key isn't in the dictionary.')
""" user = {
    'name': 'Sara',
    'age': 12
}
print(user['age'])
print(user['ago'])
print(user.get('ago', 'some thinngs is wrong')) """

#! اضافه کردن کلید و ولیو به دیکشنری
""" user = {"name": "sara", "age": 12}
user["email"] = "sabz@yahoo.com" """
#! تغییر دادن ولیو های دیکشنری
# user['age'] = 14
#! .pop() اون کلیدی که میخوایم حذف بشه رو به عنوان ورودی میدیم
# user.pop('name')
#! .popitem() از آخر دیکشنری پاک میکند
# user.popitem()
#! .clear() باعث میشه دیکشنری خالی بشه
# user.clear()
#! .keys() لیست کلید هارو نشون میده
# print(user.keys())
#! .values() لیست ولیو هارو نشون میده
# print(user.values())
#! del هم باعث میشه که کلا پاک بشه
""" del user
del user['name']
print(user) """

#! حلقه زدن در دیکشنری
# کلید ها برمیگردن
# 1:
""" for i in user:
    print(i) """
# 2:
""" for i in user.keys():
    print(i) """
# @ برای دسترسی به ولیو ها 2 تا راه هست
# 1:
""" for i in user.values():
    print(i) """
# 2:
""" for i in user:
    print(user[i]) """
#! .items() در حلقه
""" for i, j in user.items():
    print(i, ":", j) """

# ساخت دیکشنری با کمک حلقه در یک خط
""" user = {"name": "sara", "age": 12}
x = {i.title(): j for i, j in user.items()}
print(x) """
""" user = {"ali": 14, "sara": 12, "mom": 15}
x = {i.title(): j for i, j in user.items() if len(i)==3 and j%5 == 0}
print(x) """

#! While
'''for i in range(1,10,2):
    print(i)

i = 1
while i <10: #stop
    print(i)
    i +=1 #step'''

'''i = 1
while i<10:
    print(i)
    if i % 2 == 0:
        break
    i += 1'''

'''i = 0
while i<10:
    i += 1
    if not i % 2 == 0:
        continue
    print(i)'''

# while True:
#     text = input('Enter Text:')
#     if text == 'stop':
#         break

#! بازی حدس زدن شماره
# answer = int(input('player1: please insert the number (1-100):'))
# try_count = 0
# while try_count < 3:
#     guess = int(input('player2: guess a number:'))
#     if guess == answer:
#         print('player2: you won!')
#         break
#     elif guess > answer:
#         print('your guess is big!')
#         try_count += 1
#     else:
#         print('your guess is small!')
#         try_count += 1

# if try_count == 3:
#     print('player2: you lost')

# بازی سنگ کاغذ قیچی
'''while True:
    player1 = input('player1 choice(rock, paper, scissors) or exit:')
    if player1.lower() == 'exit':
        print('game over,goodbye!')
        break
    player2 = input('player2 choice(rock, paper, scissors) or exit:')
    options = ['rock', 'paper', 'scissors']
    if player1 not in options or player2 not in options:
        print('please enter a valid choice')
        continue
    print(f'player 1 choice: {player1}\nplayer2 choice:{player2}')
    if player1 == player2:
        print('it is tie')
    elif (player1 == 'rock' and player2 == 'scissors')\
    or (player1 == 'paper' and player2 == 'rock')\
    or (player1 == 'scissors' and player2 == 'paper'):
        print('player1 win')
    else:
        print('player2 win')'''

# تعریف توابع
# def welcome():
#     """ داخل تابع کامنت گذاشتنی از داک استرینگ استفاده میشود """
#     print('welcome')
# welcome()

# def sadbar():
#     text = input('enter the text:')
#     for i in range(1,101):
#         print(text)
# sadbar()

# odd_even
# def odd_even():
#     num = int(input('enter the number1:'))
#     if num %2 == 0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')
# odd_even()

# def info(name, family, age=13, From='Iran'):
#     print(12*'*')
#     print(f'name:{name}\nfamily:{family}\nage:{age}\nfrom:{From}')
#     print(12*'*')
# info('ali', 'malekzadeh', 21, 'Iran')
# info('sara', 'alizadeh', 13, 'Iran')
# info('mina', 'alizadeh', 13, 'Iran')

