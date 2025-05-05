import math

def get_username():
    user = input('Please Enter your name: ')
    return user


def get_packing_num(user):
    num_items = int(input( 'Hello ' + user + '! How many number of items are there:'))
    items_pbox = int(input('How many items per box: '))
    pack_amount = math.ceil(num_items / items_pbox)
    print(user + ', thankyou for using the automated packing calculator 3000.')
    print('Based upon your inputed number we calculated the following:')
    print('For ' + str(num_items) + ' items, packing ' + str(items_pbox) + ' in each box.')
    print('You will need ' + str(pack_amount) + ' boxes.')
    
    

user = get_username()

get_packing_num(user)
