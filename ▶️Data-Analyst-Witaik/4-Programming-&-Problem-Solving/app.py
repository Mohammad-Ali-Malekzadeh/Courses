# for write comment
# دستور های گذشته رو پاک میکند cls در ترمینال با
# !string => str() => رشته
# هرچیزی که داخل دابل کوتیشن و سینگل کوتیشن قرار بگیرخ بخش میگم رشته
# با هم جمع میشوند str
# " " or ' '
# ctrl + / => # (comment)
# name= 'nima'
# text = "this is a python class"
# age = '12'
# last_name = 'alizade'
# !print(): تابعی که خروجی رو در ترمینال نشان میدهد
# print('hi '+name)
# print('hi '+name)
# در پرینت گرفتن اگر , بذاریم بین رشته ها خودش یه فاصله میذاره
# print('hi',name, last_name)
# اگر یک رشته رو ضرب در یک عدد کنیم اون استرینگ رو چند بار پرینت میکند
# print(name*3)
# هر تابع داخل پایتون یک عملی رو انجام میدهد
# len() => تعداد کاراکتر
# print(len(text))
# ! type()
# integer => int() => اعداد صحیح
# n = -1
# m = 3
# float() => اعداد صحیح
# k = 9.9
# print(n,m,k)
# نمیتونه تعداد موجود در یک عدد رو نشون بده و باید در تایپ استرینگ باشد عددمون len تابع
# print(len('09111412345'))
# type() => نوع متغییر
# print(type(m), type(k))

# در یک فایل دیگر عملیات های ریاضی روی اعداد گفته شد

# a = 10
# a/=2 #a=10/2=5.0
# print(a)

# !docstring => """ """ or ''' '''
# میشه با سه تا کوتیشن کامنت چند خطی بسازیم
""" text= '''hi
my name is: ali
my last name is: malekzadeh'''
print(text) """
# داخل استرینگ میتونیم از بک اسپیس برای اینتر زدن استفاده کنیم
# print('hello\nhow are you\nhow old are you')

# نام متغیر هر طور که تعریف کردیم به همون فرمت باید صدا کنیم. مراقب بزرگی کوچیک بودن حروف باشیم
# هنگام تعریف متغییر نمیشه اول عدد بذاریم و بعد نوشته باشه. پس باید اول یک حرف باشد
# سعی مان بر این باشد که نام متغییر معنا دار باشد
# اگر متغییر مون چند حرفی باشد بین آنها _ میگذاریم
# my_last_name = 'ali'
# کلمات کلیدی پایتون رو برای نام متغییر انتخاب نکنیم
# help('keywords')
""" from = 'iran'
print(from) """
# مینوشتیم دیگه ارور نمیداد From اگر

# !تبدیل سازی
# int(),str(),float()
# str=>int
# n = '123'
# n = int(n) #int => save
# print(n * 2)

# float => int
# m = 9.87
# print(int(m))
# اعداد اعشاری رو گرد نمیکنه و حذف میکنه که باید حواسمون به این موضوع باشدfloat => int هنگام تبدیل

# !input(str) => str
# name = input('whats your name:\n')
# last_name = input('whats your last name:\n')
# print('welcome', name, last_name)

# age = input(input('enter your age:'))
# print(age*2)

# ?تمرین
# kg => g
# kg = float(input('enter kg:'))
# print('kg => g:\n',kg,'*1000=', kg*1000,'gr')

# index => +,-
# !var[num] => str , start from 0
# name= 'this is a python class'
# print(name[3])
# print(name[-4])

# !slicing => var[start:stop-1:step]
name = "this is a python class"
# print(name[10:16])
# print(name[5:7]) #is
# print(name[-6:-2])
# print(name[8:-5])
# print(name[0:])
# print(name[::-1])

# !متدد رشته ای
# text = 'python is good for you'
# text = 'PYTHON IS GOOD FOR YOU'
# تابع هایی که یاد گرفتیم: type() len() print() input()
# print(text.upper())
# print(text.lower())
# print(text.title())
# name = input('enter your name:').strip().upper()
# print('name',name)

# strip نکته در مورد
# text = '        python is good for you   '
# print('f',text,'k')
# اگر بخوایم از سمت راست حذف کنم: lstrip
# اگر بخوایم از سمت چپ حذف کنم: rstrip
# print('f',text.rstrip,'k')
# print('f',text.lstrip,'k')

# text = "python is python good for you python"
# !replace(old,new,count)
# print(text.replace('python', 'html'))
# print(text.replace('o', 'html'))
# print(text.replace('python', 'html', 1))
# print(text.replace('python', 'html', 2))

# استفاده کنیم slicing کنیم باید از replace اگر بخواهیم از وسط ها 
# print(text[:6]+text[6:].replace('python','css',1))

# !format()
# name ='reza'
# age = 12
# !fstring
# text= 'my name is {} and my age {} ters old'.format(name,age)
# text= f'my name is {name} and my age {age} ters old'

# !count
# text = "python is python good for you python"
# print (text.count('python'))
# print (text.count('o'))

# !var[num] => str
# index(character, start) var.index(str) => num
# text = "python is python good for you python"
# print(text.index('n',16))
# print(text.index('t',13))

# ?تمرین
# ایمیل دریافت کنه و نام کاربری رو از ایمیل جدا کنه
# mina1223@yahoo.com
# ali23455@gmail.com
# nima@info.ir
# email = input('enter email:')
# name = email[:email.index('@')]
# email_name = email[email.index('@')+1:email.index('.com')]
# print(f'email:{email}\nname:{name}\nemail name:{email_name}')

# ?تمرین مشابه با تمرین بالا
# file.py => py
# text.txt => text
# img.jpg
# name_file = 'file.py'
# name = name_file[:name_file.index('.')]
# file = name_file[name_file.index('.')+1:]

# !boolean => bool()
# > <, >= <=, == != خروجی اینها بولین میباشد
# print(5>8)
# print(7==4)
# name= 'ali'
# print(name == 'sara')
# @in =>
# text = 'python is ood for you'
# print('python' in text)
# age = int(input('enter your age:'))
# ! if statement
# if age>=18:
#     print('you can drive')
# else:
#     print('you can not drive')

# @ چطور بفهمیم یک عدد زوج است؟
# num = int(input('enter your num:'))
# if num%2 == 0:
#     print(f'this number is ({num}) even')
# else:
#     print(f'this number is ({num}) odd')

# اگر شرط هامون بیشتر از یکی بود چه کنیم؟
# num1 = int(input('enter your num1:'))
# num2 = int(input('enter your num2:'))
# ope = input('enter your choice(+,-,*,/,**)')
# if ope == '+':
#     x = num1 + num2
#     print(x)
# elif ope == '-':
#     x = num1 - num2
#     print(x)
# elif ope == '*':
#     x = num1 * num2
#     print(x)
# elif ope == '/':
#     x = num1 / num2
#     print(x)
# elif ope == '**':
#     x = num1 ** num2
#     print(x)
# else:
#     print('invalid input...!!')

#! or , and
# and: زمانی درست است که هر دو شرط مون درست باشد
# or: زمانی درست است که یکی از دو شرط مون درست باشد
# print(3>9 and 8>2)
# num1 = int(input('enter your num1:'))
# num2 = int(input('enter your num2:'))
# num3 = int(input('enter your num3:'))
# if num1>num2 and num1>num3:
#     print(f'num1:{num1} is max')
# elif num2>num1 and num2>num3:
#     print(f'num2:{num2} is max')
# else:
#     print(f'num3:{num3} is max')

# print(3>8 or 2==2)
# day = int(input('enter day:'))
# if day == 1 or day == 2 or day ==3 or day ==4 or day == 5:
#     print('go to work')
# elif day ==6 or day == 7:
#     print('this is your holiday')

# if to if
# 6037-9971-0000-0000  => 16
# @isdigit(): بررسی میکنه که عدد هست یا نه
# d='sat'.isdigit()
# cart = input('enter the cart:')
# if len(cart) == 16 and cart.isdigit():
#     print('this cart is true')
#     if cart[:4] == '6037':
#         print('this cart from mali')
#     elif cart[:4] == '6219':
#         print('this cart from saman')
#     else:
#         print(" i don't know...")
# else:
#     print('cart not true...')

# ساختمان داده ها
# a = [] #list
# b = () #tuple
# c = {} #set
# d = {key:value} #dict

name = ['ali', 'mina', 'reza', 12, 2.8, True, [1,3,8,9], 'ali']
# print(name)
# print(tpe(name))
# print(len(name))
# print(name[-2])
# print(name[1:3])
# print(name[0:2])
# names = ['ali', 'mina', 'sima']
#@ .append() به آخر اضافه میکند
# names.append('sina')
#@ .index()
# names.insert(1,'amir')
# print(names)
#@ .remove()
# names.remove('mina')
#@ .pop()
# names.pop(0)
#@ extend()
# names.extend([1,2,1,3,4])
#@ .sort()
# nums = [89,23,12,78,3]
# nums.sort()
# nums.reverse()
# print(nums[::-1])
#@ .clear() توخالی میکنه
# nums.clear()
#@ del جلوش چیزی که میخوایم حذف کامل بشه رو مینویسیم
# del nums
# print(nums)