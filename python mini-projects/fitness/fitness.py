import math
from datetime import datetime

#Main and Results
def main():
   user, meters_option, feet_option, brit_stones_option = get_options()
   birth, lb, inch, gender, inch_for_feet = user_input(user, meters_option, feet_option, brit_stones_option)
   age = compute_age(birth)
   weight = kg_from_lb(lb)
   height = cm_from_in(inch)
   bmi = body_mass_index(weight, height)
   bmr = basal_metabolic_rate(gender, weight, height, age)

   #Results
   print (f'Age (years): {age:.0f}')
   if brit_stones_option == 'y':
        print (f'Weight(stones): {weight * 0.157473:.2f}')
   else:
        print (f'Weight(kg): {weight:.2f}')
   if meters_option == 'y':
        print (f'Height(m): {height * 0.01:.2f}')
   elif feet_option == 'y':
        print (f'Height(ft): {inch / 12:.0f}')
        print (f'Height(in): {inch_for_feet:.0f}')
   else:
        print (f'Height(cm): {height:.1f}')
   print (f'Body Mass Index: {bmi:.1f}')
   print (f'Basal Metabolic Rate (Kcal/Day): {bmr:.0f}')

#Calulator Options
def get_options():
    print('Hello, my name is F.I.N!')
    print('Otherwise, known as the Fitness Intelligence Network.')
    user = input('Whats your name?:')
    print('Hello, '+ user + ' lets go over some settings shall we?')
    meters_option = input('Would you like to use meters for your height instead of the default inches?(Y or N): ').lower()
    if meters_option == 'n':
       feet_option = input('Would you like to use feet and inches for your height instead of the default inches?(Y or N): ').lower()
    else:
        feet_option = 'n'
    brit_stones_option = input('Would you like to use British Stones for your weight input instead of Pounds?(Y or N): ').lower()
    if brit_stones_option == 'y':
        return user, meters_option, feet_option, brit_stones_option
    else:
        brit_stones_option = 'n'
        return user, meters_option, feet_option, brit_stones_option
        

#Gathering of User input
def user_input(user, meters_option, feet_option, brit_stones_option):
    print('Okay, ' + user + ' the next step is to get all your data! ')
    gender = input("what is your geneder (m or f): ").lower()
    birth = input("What is your birthday (yyyy-mm-dd): ")
    #weight conversions and input
    #british stones
    if brit_stones_option == 'y':
        brit_stones = float(input("What is your weight in british stones: "))
        #british stones to lb
        lb = brit_stones * 14
    else:
        #pounds input 
        lb = float(input("What is your weight in pounds: "))
    #height conversions and input
    #meters to inches
    if meters_option == 'y':
        meters= float(input("what is your height in meters: "))
        inch = meters * 39.3701
    elif feet_option == 'y':
        #feet and inches to just inches
        feet = float(input("what is your height in feet (you will be asked for inches next): "))
        inch_for_ft = float(input("and how many inches: "))
        inch = (feet * 12) + inch_for_ft
    else:
        #just inches no conversion
        inch = float(input("what is your height in inches: "))
    
    if feet_option == "y":
        return birth, lb, inch, gender, inch_for_ft
    else:
        inch_for_ft = 0
        return birth, lb, inch, gender, inch_for_ft



#Detrimination of Age from given birthday
def compute_age(birth):
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthday.year
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1
    return years


#Conversion of lb to kg
def kg_from_lb(lb):
    kg = 0.45359237 * lb
    return kg

#conversion of in to cm
def cm_from_in(inch):
    cm = 2.54 * inch
    return cm

#Calculations for BMI
def body_mass_index(weight, height):
    bmi = (10000 * weight) / pow(height, 2)
    return bmi

#Calculation for BMR
def basal_metabolic_rate(gender, weight, height, age):
    if gender == "f":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    elif gender == "m":
        bmr = bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        print("Sorry, it seems there was an error. Please make sure you filled out everything correctly and try again.")
    return bmr

#Call of Main() function
main()