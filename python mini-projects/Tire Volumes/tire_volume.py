import math
from datetime import datetime

#User Identification
def get_username():
    username = input("Please enter your name:")
    return username

#Gathering of User Input and Calulations
def get_tire_dimensions(username):
    print ('Hello ' + username + ' welcome to the tire volume system. Please awnser the following three questions:' )
    width = float(input ('What is the width of the tire in milimeters: '))
    aspect = float(input('What is the aspect ratio of the tire: '))
    diameter = float(input('What is the diameter of the wheel in inches: '))
    volume = (math.pi * math.pow(width, 2) * aspect * (width * aspect + 2540 * diameter)) / 10000000000
    print (f'The estimated volume of the tire is {volume:.2f}')
    return volume, width, aspect, diameter

#Gathering of system date
def get_system_date():
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%Y-%m-%d}")
    return current_date_and_time



#Customer Price notifications
def get_estimated_prices(diameter):
    print('Based on the specifications you have given me these are the estimated price ranges for new tires according to DiscountTire:')
    if diameter <= 11:
        print("The tire size of "  + str(diameter) + " inches that you have specified is smaller than anything discount tire currently holds. There for we have no estimated price. Sorry for this inconvienvces.")
    elif diameter <= 15:
        print("For a tire size of " + str(diameter) + " inches All SEASON tires will cost aprox. $80-$150 per tire.")
        print("For a tire size of " + str(diameter) + " inches WINTER/SNOW tires will cost aprox. $100-$150 per tire.")
    elif diameter <= 20:
        print("For a tire size of " + str(diameter) + " inches All SEASON tires will cost aprox. $100-$250  per tire.")
        print("For a tire size of " + str(diameter) + " inches WINTER/SNOW tires will cost aprox. $200-$400 per tire.")
        print("For a tire size of " + str(diameter) + " inches ALL TERRAIN tires will cost aprox. $150-$250 per tire.")
        print("For a tire size of " + str(diameter) + " inches PERFORMACE tires will cost aprox. $100-$750 per tire.")
    elif diameter <= 26:
         print("For a tire size of " + str(diameter) + " inches All SEASON tires will cost aprox. $140-$170  per tire.")
         print("For a tire size of " + str(diameter) + " inches ALL TERRAIN tires will cost aprox. $200-$500 per tire.")
         print("For a tire size of " + str(diameter) + " inches PERFORMACE tires will cost aprox. $200-$1000 per tire.")
    else:
        print("The tire size of "  + str(diameter) + " inches that you have specified is larger than anything discount tire currently holds. There for we have no estimated price. Sorry for this inconvienvces.")

#confirm customer stance and get contact info
def get_customer_commitment(username):
   stance = str(input( username + " based upon the estimated prices. Would you be interested in talking with a representitve? Please awnser yes or no:")).lower()
   if stance == "yes":
       print("Perfect! Thank you for choosing us. PLease put in your cell phone number and a representitve will get in contact with you shortly")
       phone_number = str(input("Type your phone number here [i.e xxx-xxx-xxxx] --->"))
       return phone_number, stance 
   elif stance == "no":
       print("No worries! Please keep us in mind for when you do need a new tire. Also know that we do price match!")
       return stance
   else:
       print("Sorry it seems you awnsered our question with something other than yes or no. Please reach out to a represtitive at 413-227-5645, if you have any further questions. Sorry for any inconvincence" )
       return stance

#Creating txt document

def get_txt_creation(current_date_time, volume, width, aspect, diameter, username, phone_number, stance):
    if stance == "yes":
        with open("volumes.txt", "at") as volume_file:
         print(f"{current_date_time:%Y-%m-%d}, {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume:2f}, Customer is interested in possible purchase. Contact info is {phone_number}", file=volume_file)
    elif stance =="no":
        with open("volumes.txt", "at") as volume_file:
         print(f"{current_date_time:%Y-%m-%d}, {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume:2f}", file=volume_file)     
    print (username + " a file named volumes.txt has been created with the specificed arguments you provided and the volume calaculations.")

#functions calls
def main():
    username = get_username()
    volume, width, aspect, diameter = get_tire_dimensions(username)
    current_date_time = get_system_date()
    get_estimated_prices(diameter)
    phone_number, stance = get_customer_commitment(username)
    get_txt_creation(current_date_time, volume, width, aspect, diameter, username, phone_number, stance)
    input()

main()
