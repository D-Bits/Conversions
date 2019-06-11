from temperature import farenheit_to_celsius, celsius_to_farenheit
from lengths import feet_to_meters, meters_to_feet, miles_to_kilos


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

    conversion = int(input('Enter one of the above integers to specify a conversion: '))

    if conversion == 1:
        farenheit_to_celsius()
    elif conversion == 2:
        celsius_to_farenheit()
    elif conversion == 3:
        feet_to_meters()
    elif conversion == 4:
        meters_to_feet()
    elif conversion == 5:
        miles_to_kilos()
    
    else:
        raise Exception('Invalid value entered.')