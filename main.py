from temperature import(
    fahrenheit_to_celsius, 
    celsius_to_fahrenheit, 
    celsius_to_kelvin, 
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit
)
from lengths import( 
    feet_to_meters, 
    meters_to_feet, 
    miles_to_kilometers, 
    kilometers_to_miles
)
from mass import(
    pounds_to_kilograms,
    kilograms_to_pounds
)

options = {
    '1': 'Fahrenheit to Celsius',
    '2': 'Celsius to Fahrenheit',
    '3': 'Celsius to Kelvin',
    '4': 'Kelvin to Celsius',
    '5': 'Fahrenheit to Kelvin',
    '6': 'Kelvin to Fahrenheit',
    '7': 'Feet to Meters',
    '8': 'Meters to Feet',
    '9': 'Miles to Kilometers',
    '10': 'Kilometers to Miles',
    '11': 'Pounds to Kilograms',
    '12': 'Kilograms to Pounds'
}


if __name__ == "__main__":
    
    for key, val in options.items():
        
        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a conversion: '))
    print()

    if conversion == 1:
        fahrenheit_to_celsius()
    elif conversion == 2:
        celsius_to_fahrenheit()
    elif conversion == 3:
        celsius_to_kelvin()
    elif conversion == 4:
        kelvin_to_celsius()
    elif conversion == 5:
        fahrenheit_to_kelvin()
    elif conversion == 6:
        kelvin_to_fahrenheit()
    elif conversion == 7:
        feet_to_meters()
    elif conversion == 8:
        meters_to_feet()
    elif conversion == 9:
        miles_to_kilometers()
    elif conversion == 10:
        kilometers_to_miles()
    elif conversion == 11:
        pounds_to_kilograms()
    elif conversion == 12:
        kilograms_to_pounds()
    else:
        raise Exception('Invalid value entered.')