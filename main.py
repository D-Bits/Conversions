from temperature import fahrenheit_to_celsius, celsius_to_fahrenheit, celsius_to_kelvin, kelvin_to_celsius
from lengths import feet_to_meters, meters_to_feet, miles_to_kilometers, kilometers_to_miles


options = {
    '1': 'Fahrenheit to Celsius',
    '2': 'Celsius to Fahrenheit',
    '3': 'Celsius to Kelvin',
    '4': 'Kelvin to Celsius',
    '5': 'Feet to Meters',
    '6': 'Meters to Feet',
    '7': 'Miles to Kilometers',
    '8': 'Kilometers to Miles'
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
        feet_to_meters()
    else:
        raise Exception('Invalid value entered.')