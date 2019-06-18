
temp_options = {
    '1': 'Fahrenheit to Celsius',
    '2': 'Celsius to Fahrenheit',
    '3': 'Celsius to Kelvin',
    '4': 'Kelvin to Celsius',
    '5': 'Fahrenheit to Kelvin',
    '6': 'Kelvin to Fahrenheit',
}

"""
Throw exception if input is < absolute zero
"""

def fahrenheit_to_celsius():

    fahrenheit = float(input('Enter an amount in fahrenheit to be converted to celsius: '))
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!')
    celsius = (fahrenheit -32) / 1.80
    rounded = round(celsius, 2)

    print(f'{fahrenheit} degrees F equals {rounded} degrees C.')


def celsius_to_fahrenheit():

    celsius = float(input('Enter an amount in celsius to be converted to fahrenheit: '))
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!')
    fahrenheit = celsius * 1.80 + 32.00
    rounded = round(fahrenheit, 2)

    print(f'{celsius} degrees C equals {rounded} degrees F.')
    

def celsius_to_kelvin():
    
    celsius = float(input('Enter an amount in celsius to be converted to Kelvin: '))
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!')
    kelvin = celsius + 273.15
    rounded = round(kelvin, 2)

    print(f'{celsius} degrees C equals {rounded} K.')


def kelvin_to_celsius():
    
    kelvin = float(input('Enter an amount in Kelvin to be converted to celsius: '))
    if kelvin < 0:
        raise Exception('Cannot be below absolute zero!')
    celsius = kelvin - 273.15
    rounded = round(celsius, 2)

    print(f'{kelvin} degrees K equals {rounded} degrees C.')


def fahrenheit_to_kelvin():

    fahrenheit = float(input('Enter an amount in fahrenheit to be converted to Kelvin: '))
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!')
    kelvin = ((fahrenheit - 32) / 1.80)+ 273.15
    rounded = round(kelvin, 2)

    print(f'{fahrenheit} degrees F equals {rounded} degrees K.')


def kelvin_to_fahrenheit():

    kelvin = float(input('Enter an amount in fahrenheit to be converted to Kelvin: '))
    if kelvin < 0:
        raise Exception('Cannot be below absolute zero!')
    fahrenheit = (kelvin - 273.15) * 1.80 + 32
    rounded = round(fahrenheit, 2)

    print(f'{kelvin} degrees K equals {rounded} degrees F.')


# Display the available unit conversions, prompt the user to choose
def temp_choices():

    print()

    for key, val in temp_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a temperature conversion: '))
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
    else:
        raise Exception('Invalid value entered.')