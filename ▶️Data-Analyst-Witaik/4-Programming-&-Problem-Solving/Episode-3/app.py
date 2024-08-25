#? ali => ila  reverse String
""" def revers_str(string):
    x = string[::-1]
    #! return خروجی تابع رو مشخص میکند
    return x
print(revers_str('ali')) """

#? تابع نمایش شماره کارت
# 6037997100001111
""" def test(card):
    x = '*' * 12 + card[-4:]
    return x
print(test('6037997100001111')) """


#? حذف تکراری ها از لیست
""" def test(list_name):
    x = list(set(list_name))
    x.sort()
    return x
a = ['z', 'l', 'b', 'c', 'e', 'z']
print(test(a)) """

#? محاسبه میانگین سن های افراد
""" def cal(grades):
    total = sum(grades.values())
    ave = total/len(grades)
    return ave
g = {
    'alice': 85,
    'bob' : 90,
    'diavid': 90
}
print(cal(g)) """

