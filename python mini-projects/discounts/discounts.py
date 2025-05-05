"""
import math

from datetime import datetime

today = datetime.now()

print(f'Day:' + str(today.weekday()))

week_day = datetime.now()
print(week_day.strftime("%A"))

subtotal = float(input('What is your subtotal? '))

if subtotal >= 50.00 and (today.weekday() == 1 or today.weekday() == 2):
    discount_rate = .10
else:
    discount_rate = 0

discount = subtotal * discount_rate
tax_rate = .06
tax = (subtotal - discount) * tax_rate
total = tax + subtotal
print(f'Subtotal: {subtotal:.2f}')
print(f'Discount: {discount:.2f}')
print(f'Tax: {tax:.2f}')
print(f'Total due: {total:.2f}')

"""


import math 
from datetime import datetime

#getting the day of the week
def get_current_day():
    today = datetime.now()
    day_of_week = today.weekday()
    return day_of_week

#determination of if discount gets applied
def get_discount_application(day_of_week):
    if day_of_week == 1 or 2:
        final_total = get_tuesday()
        return final_total
    else:
       final_total = get_monday()
       return final_total

#Function for normal pricing conventions       
def get_monday():
    subtotal = float(input("Please enter your subtotal?"))
    total = subtotal + (subtotal * .06)
    return total

#function for discounted conventions
def get_tuesday():
    discount = .10
    subtotal = float(input("Please enter your subtotal?"))
    if subtotal >= 50.00:
        discounted_price = subtotal - (subtotal * discount )
    total = discounted_price + (discounted_price * .06)
    return total

day_of_week = get_current_day()

print(f'Total Due: {get_discount_application(day_of_week):.2f}')

