# If you want to see more beautiful comments, install this extension: https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments


# *------------------------------------#
# *------------Fastness-Team-----------#
# *------------Python-Section----------#
# *--------------Practice-1------------#
# *------------------------------------#

#? take input from the user about the practice number  and who wrote the practice
select_pr = "n_" + input("Please Select one of the practices (1 - 5): ")
select_person = (int(input("\nFastness Team members are:\n1- 👩Sepideh\n2- 👨Alireza\n3- 🧑Mohammd Ali\nplease chose one of them: "))- 1)

#? Global Variables
# practice 2
hamrahe_aval = ["0991", "0992", "0912", "0910", "0919", "0911", "0913", "0914", "0915", "0916", "0917", "0918", "0990", "0993"]
irancel = ['0930', '0933', '0935', '0936', '0937', '0938', '0939', '0901', '0902', '0903', '0905'] 
raitel = ['0920', '0921', '0922', '0923']
# practice 3
text = 'Today the weather is wonderful, the sun is smiling at me and I feel good'

#! Sepideh
def pr1_sepideh():
    site_name=input('enter site name:')
    n=len(site_name)
    n1=site_name.index('.')
    n2=site_name.index('.',n1+1,n)
    print(f'domain:{site_name[0:n1]}')
    print(f'company:{site_name[n2+1:n+1]}')


def pr2_sepideh():
    num=input("enter the number \n")
    n=len(num)
    if n!=11:
      print('the number is not correct')
    elif num[2]==( '0') or num[2]=='3':
      print('irancell')
    elif num[2]==( '1') or num[2]=='9':
      print('hamrah aval')
    elif num[2]=='2' :
      print('ritel')


def pr3_sepideh():
    print(text.replace('weather','wemmther'))


def pr4_sepideh():
    buy1=int(input( 'enter your first purchase: '))
    buy2=int(input( 'enter your next purchase: '))
    buy3=int(input( 'enter your next purchase: '))
    if buy1+buy2+buy3> 200:
      print("it's over")
    cash=200-(buy1+buy2+buy3)
    print(cash)


def pr5_sepideh():
    a=int(input('enter the dimension of square'))
    primeter=4*int(a)
    area=a*a
    print(f'primeter of an square with {a} meter(s) side is {primeter} with area {area}')

    a=float(input('enter the first dimension of the first side of triangle'))
    b=float(input('enter the second dimension of the triangle'))
    c=float(input('enter the third dimensions of  the triangle'))
    if (a+b>c and a+c>b and b+c>a):
      s=(a+b+c)/2
      s1=a+b+c
      area=(s*(s-a)*(s-b)*(s-c))**0.5
      print(f'arae is {area} and primeter is {s1}')
    else:
      print('impossible, enter another 3 dimensions')


#! Alireza
def pr1_alireza():
    #Sure! Here is a Python code that takes a website domain as input and splits it into three discrete outputs:

    def split_domain(domain):
        parts = domain.split('.')

        if len(parts) >= 3:
            output1 = parts[0]
            output2 = parts[1]
            output3 = '.'.join(parts[2:])

            return output1, output2, output3
        else:
            return "Invalid domain format"

    # Get website domain from user input
    website_domain = input("Enter website domain: ")

    # Split the domain into three parts
    output1, output2, output3 = split_domain(website_domain)

    print("First part of domain:", output1)
    print("Second part of domain:", output2)
    print("Third part of domain:", output3)

#You can run this code in a Python environment, enter a website domain when prompted, and it will split the domain into three parts for you.


def pr2_alireza():
    def validate_phone_number(number):
        # Check if the entered number is in any of the lists
        if number[:4] in hamrahe_aval:
            return "Hamrah_aval"
        elif number[:4] in irancel:
            return "Irancell"
        elif number[:4] in raitel:
            return "Rightel"
        else:
            return "Unknown category"

    # Example usage:
    user_input = input("Enter a phone number: ")
    if validate_phone_number(user_input):
        category = validate_phone_number(user_input)
        print(f"Category: {category}")
    else:
        print("Invalid phone number")


def pr3_alireza():
    new_text = text.replace("weather", "wemmther")
    print(new_text)


def pr4_alireza():
    def calculate_purchase(total_cash, item_prices):
        total_paid = sum(item_prices)
        cash_in_hand = total_cash - total_paid
        can_buy_more = cash_in_hand > 0
        return total_paid, cash_in_hand, can_buy_more

    # Example usage
    total_cash = 200  # Initial cash
    item_prices = [50, 30, 20]  # Prices of items the customer wants to buy
    
    total_paid, cash_in_hand, can_buy_more = calculate_purchase(total_cash, item_prices)
    
    print(f"Total paid: ${total_paid}")
    print(f"Cash in hand: ${cash_in_hand}")
    print(f"Can buy more items: {'Yes' if can_buy_more else 'No'}")



def pr5_alireza():
    def calculate_triangle_area(s1, s2, s3):
        # Calculate the perimeter
        perimeter = s1 + s2 + s3
        # Calculate the semi-perimeter
        s = perimeter / 2
        # Calculate the area using Heron's formula
        area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
        return area, perimeter

    def calculate_square_area(side_length):
        # Calculate the area
        square_area = side_length ** 2
        # Calculate the perimeter
        square_perimeter = 4 * side_length
        return square_area, square_perimeter

    # Get user input
    shape_name = input("Enter the shape (triangle or square): ")

    if shape_name == "triangle":
        s1 = int(input("Enter the first side of the triangle: "))
        s2 = int(input("Enter the second side of the triangle: "))
        s3 = int(input("Enter the third side of the triangle: "))
        result_triangle = calculate_triangle_area(s1, s2, s3)
        tri_area = result_triangle[0]
        tri_perimeter = result_triangle[1]
        print(f"The area of the triangle is: {tri_area:.2f}")
        print(f"The perimeter of the triangle is: {tri_perimeter:.2f}")
    elif shape_name == "square":
        side_length = int(input("Enter the side length of the square: "))
        result_triangle = calculate_square_area(side_length)
        sqt_area = result_triangle[0]
        sqt_perimeter = result_triangle[1]
        print(f"The area of the square is: {sqt_area:.2f}")
        print(f"The perimeter of the square is: {sqt_perimeter:.2f}")
    else:
        print("Invalid shape name. Please enter 'triangle' or 'square'.")


#! Mohammad Ali
def pr1_mohammad_ali():
    web = input("Please Enter a web site: ")
    # delete 'www.' from input
    if web.count(".") > 1:
        web = web[4:]
    domain = web[web.indpr(".") :]
    name = web[: web.indpr(".")]
    print(f"Your site Domain: {domain}\nYour site Name: {name}")


def pr2_mohammad_ali():
    number = input('Please Write a phone number: ')
    if len(number) != 11:
        print('your namber is invalid :_(')
    else:
        if number[:4] in hamrahe_aval:
            print('your phone number is Hamrahe aval.')
        elif number[:4] in irancel:
            print('your phone number is Irancel.')
        elif number[:4] in raitel:
            print('your phone number is Raitel.')


def pr3_mohammad_ali():
    result = text[:text.index('w')] + text[text.index('w'):text.index('r')].replace('a','mm') + text[text.index('er '):]
    print(result)


def pr4_mohammad_ali():
    print("Welcome to 🍇 Fruit shop 🍇")
    balance = 200
    fruits = {
            'banana': [10,0],
            'milk': [6,0],
            'apple': [3,0],
            'potato': [1,0]
        }

    while balance >= fruits['potato'][0]:
        shop = int(input(f'\nYour balance: {str(balance)}\nlist of fruits:\n1- 🍌banana({str(fruits['banana'][1])}): {str(fruits['banana'][0])}$\n2- 🥛milk({str(fruits['milk'][1])}): {str(fruits['milk'][0])}$\n3- 🍎apple({str(fruits['apple'][1])}): {str(fruits['apple'][0])}$\n4- 🥔potato({str(fruits['potato'][1])}): {str(fruits['potato'][0])}$\n(if you want leave shop wite: 0)\nPlease chose your Fruit: ')) - 1

        # for invalid input or exit from shop
        if shop not in [-1,0,1,2,3]:
            print("Please Enter a Valid input!!!")
            quit()
        elif shop == -1:
            break

        # calculate balance and number of fruits
        balance -= list(fruits.values())[shop][0]
        if balance < 0:
            balance += list(fruits.values())[shop][0]
            continue
        list(fruits.values())[shop][1] += 1
    
    # print report of shop :)
    print(f'\nReport Your Shop:\nYour balance: {str(balance)}\n1- 🍌banana({str(fruits['banana'][1])})\n2- 🥛milk({str(fruits['milk'][1])})\n3- 🍎apple({str(fruits['apple'][1])})\n4- 🥔potato({str(fruits['potato'][1])})')


def pr5_mohammad_ali():
    shape = int(input('Please select one of this shape:\n1- ⏹️Rectangle\n2- 🔼Triangle\n ..? '))
    if shape == 1:
        length = int(input('Please Enter Length: '))
        width = int(input('Please Enter Width: '))
        print(f'The area of ​​the rectangle is equal to: {length * width}')
    elif shape == 2:
        base = int(input('Please Enter base: '))
        height = int(input('Please Enter height: '))
        print(f'The area of ​​the Radius is equal to: {(base * height)/2}')


#? System of Choosing the Practice
practices = {
    "n_1": [pr1_sepideh, pr1_alireza, pr1_mohammad_ali],
    "n_2": [pr2_sepideh, pr2_alireza, pr2_mohammad_ali],
    "n_3": [pr3_sepideh, pr3_alireza, pr3_mohammad_ali],
    "n_4": [pr4_sepideh, pr4_alireza, pr4_mohammad_ali],
    "n_5": [pr5_sepideh, pr5_alireza, pr5_mohammad_ali],
}

if select_pr in practices and select_person in [0, 1, 2]:
    practices[select_pr][select_person]()
else:
    print("Please Enter a Valid input!!!")
    quit()