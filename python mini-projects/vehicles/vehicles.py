# vehicles.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

def main():
    # Create a dictionary that contains data about six vehicles.
    # The key for each vehicle in the dictionary is the vehicle's
    # identification number (VIN). The value for each vehicle is
    # a list that contains the year, manufacturer, model, color,
    # engine design, and engine displacement.
    vehicles = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        #0
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        #2
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        #3
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        #4
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        #5
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        #6
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }

    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3

    # Ask the user for a vehicle identification number (VIN).
    vin = input("Please enter a VIN: ")

    # Check if the vin is a key that is in the vehicles dictionary.
    if vin in vehicles:
        print('We found a recored that matches your query.')
        print("Please wait a moment as we pull up the vehicles info.")

        # Find the data for the vehicle that the user wants.
        car_info = vehicles[vin]

        # Print the manufacturer, model, and color of the vehicle.
        # Don't print the year, engine design, or displacement.
        manufacturer = car_info[MANUFACTURER_INDEX]
        model = car_info[MODEL_INDEX]
        color= car_info[COLOR_INDEX]
        print(manufacturer, model, color)

    else:
        # Print a message stating that the VIN entered
        # by the user is not in the dictionary.
        print(f"{vin} is not in the dictionary.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
