import csv
from os import access
import pprint
from datetime import datetime

def read_products(filename):
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row[0]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row[1], float(row[2])

    # Return the dictionary.
    return dictionary

def reciept_item_print(reader, products_dict):
    #indexs for products.csv
    NAME_INDEX = 0
    PRICE_INDEX = 1

    #indexs for reques.csv
    PRODUCT_NUM_INDEX = 0
    QUANTITY_INDEX = 1

    num_items = 0
    sub_total = 0
    recipt_contents_list = []
    for request in reader:
        #Pulls product ID from request.csv
        product_id = request[PRODUCT_NUM_INDEX]

        #pulls product amount from request.csv
        amount = request[QUANTITY_INDEX]

        #pulls product inforamtion from products.csv
        item = products_dict[product_id]

        #pulls product name from products.csv
        product_name = item[NAME_INDEX]

        #pulls the product price
        product_price = item[PRICE_INDEX]

        #adding loop statemnents
        num_items += int(amount)
        sub_total += float(amount) * float(product_price)

        #creation of one line entry on recipt 
        recipt_contents_list.append(f"{product_name}: {amount} @ ${product_price}")
        

    return num_items, sub_total, recipt_contents_list
    
def recpit_stats_print(num_items, sub_total, current_date_and_time, access = 'denied'):
    recipt_stat_list = []
    if access == 'granted':
        dis_aprov = input('Would you like to add a discount? (y or n): ')
        
        if dis_aprov == 'y':
            discount = float(input('How much would you like to discount of the sub total?'\
                '(ie .1 for 10%, .25 for 25%): '))

           
            #Calculations for prices and payment
            discount_price = sub_total * discount
            discount_sub_total = sub_total - discount_price
            sales_tax = discount_sub_total * .06
            total = discount_sub_total + sales_tax

            print()
            recipt_stat_list.append(f'Number of Items: {num_items}')
            recipt_stat_list.append(f'Subtotal: ${sub_total:.2f}')
            recipt_stat_list.append(f'Subtotal w/ discount: ${discount_sub_total:.2f}')
            recipt_stat_list.append(f'Sales Tax: ${sales_tax:.2f}')
            recipt_stat_list.append(f'Total: ${total:.2f}')
            recipt_stat_list.append(f'You saved ${discount_price:.2f}')
            recipt_stat_list.append('')
            recipt_stat_list.append(f'Thank you for shopping at Safeway Grocery.')
            recipt_stat_list.append(f"{current_date_and_time:%c}")
        else:
            #Calculations for prices and payment
            sales_tax = sub_total * .06
            total = sub_total + sales_tax

            recipt_stat_list.append('')
            recipt_stat_list.append(f'Number of Items: ${num_items}')
            recipt_stat_list.append(f'Subtotal: ${sub_total:.2f}')
            recipt_stat_list.append(f'Sales Tax: ${sales_tax:.2f}')
            recipt_stat_list.append(f'Total: ${total:.2f}')
            recipt_stat_list.append('')
            recipt_stat_list.append(f'Thank you for shopping at Safeway Grocery.')
            recipt_stat_list.append(f"{current_date_and_time:%c}")
    
    
    else:    
        #Calculations for prices and payment
        sales_tax = sub_total * .06
        total = sub_total + sales_tax

        recipt_stat_list.append('')
        recipt_stat_list.append(f'Number of Items: ${num_items}')
        recipt_stat_list.append(f'Subtotal: ${sub_total:.2f}')
        recipt_stat_list.append(f'Sales Tax: ${sales_tax:.2f}')
        recipt_stat_list.append(f'Total: ${total:.2f}')
        recipt_stat_list.append('')
        recipt_stat_list.append(f'Thank you for shopping at Safeway Grocery.')
        recipt_stat_list.append(f"{current_date_and_time:%c}")
    
    return recipt_stat_list

def boot_up():
    
    print('Welcome to the Zeniith, your one stop solution for online shopper proccessing')

    print()

    system_perm = input('Are you wanting to enter the system today?' \
        'If not, you will not be able to adjust any reciepts. (y or n): ')

    if system_perm == 'y':
        user_database = {
        # User: [name , password]
        "nburnett":	["Nathan","lionking"],
        "jsmith":	["John", "silversurf"],
        "srogers":	["Steve","starwars"],
        }

        userCorrect = False
        while not userCorrect:
            name = input('Username: ')
            usercheck, user = user_check(user_database, name)
            if usercheck != 'True': #checks the username typed in
                print ('Invalid username.')
                continue
            else:
                print (f'Hello, {user[0]}.')
                userCorrect = True


        passCorrect = False
        while not passCorrect:
            password = input('Password: ')
            passcheck = pass_check(user, password)
            if passcheck != 'True': #checks the password typed in
                print ('Password incorrect.')
                continue
            else:
                passCorrect = True

        # Since password is correct, continue.
        print ('Password correct.')
        print ('Logging in...')
        print ('Logged in.')

        access = 'granted'

    else:
        access = 'denied'
    
    return access    

def user_check(user_database, name):
    if name in user_database:
        user = user_database[name]
        user_check = 'True'
    else:
        user_check = 'False'
        user = 'invalid' 
    
    return user_check, user

def pass_check(user, password):
    if password == user[1]:
        pass_check = 'True'
    else:
        pass_check = 'False' 
    
    return pass_check

def recipt_creation(reciept, stats):
    print()
    print('Safeway Grocery')
    print()
    print(*reciept, sep = "\n")
    print()
    print(*stats, sep = "\n")

def main():
    try: 
        access = boot_up()

        current_date_and_time = datetime.now()
        filename = 'products.csv'
        # reads and writes products.csv
        products_dict = read_products(filename)
        pprint.pprint(products_dict)

        # Open a file named request.csv and store a reference
        # to the opened file in a variable named request_file.
        with open("request.csv", "rt") as request_file:

            # object that will read from the opened file.
            reader = csv.reader(request_file)

            # statement skips the first line of the CSV file.
            next(reader)

            #Prints the Item list with the amount and price respectivly
            #Also Calculates sub_total and number of items
            num_items, sub_total, reciept_content_list = reciept_item_print(reader, products_dict)

            #Calculates remaining values such as tax and total. Also prints
            #Prints remaing information such as number of items
            recpit_stat_list = recpit_stats_print(num_items, sub_total, current_date_and_time, access)

            recipt_creation(reciept_content_list, recpit_stat_list)

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")
    
    except KeyError as key_err:
        print()
        print(type(key_err).__name__, key_err, sep=": ")
        print(f'The item {key_err} that is trying to be '\
            'requested does not exist in the products database')
        print('Please make sure it is a valid item and '\
            'try again')

if __name__ == "__main__":
    main()

