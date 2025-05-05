import math

#Conversion of Miles Per Gallon
def miles_per_gallon(start, end, gallons):
    mpg = (end - start) / gallons
    return mpg

#Conversion from MPG to kilometers
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

#Main function
def main():
    start = float(input('What is your starting odometer value: '))
    end = float(input('What is your ending odometer value: '))
    gallons = float(input('what was the amount of fuel you used in gallons: '))
    mpg =miles_per_gallon(start, end, gallons)
    lp100k = lp100k_from_mpg(mpg)
    print('Thank you for using the MPG to lp100k calculator! Your conversion is as follows:')
    print(f"You used {mpg:.1f} which converts to {lp100k:.2f} liters per 1000 kilometers."  )

main()
