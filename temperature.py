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

def fahrenheit_to_celsius(fahrenheit):

    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!\n')
    celsius = (fahrenheit -32) / 1.80

    return round(celsius, 2)


def celsius_to_fahrenheit(celsius):

    fahrenheit = celsius * 1.80 + 32.00
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!\n')

    return round(fahrenheit, 2)


def celsius_to_kelvin(celsius):

    kelvin = celsius + 273.15
    if celsius < -273.15:
        raise Exception('Cannot be below absolute zero!\n')

    return round(kelvin, 2)


def kelvin_to_celsius(kelvin):

    celsius = kelvin - 273.15
    if kelvin < 0:
        raise Exception('Cannot be below absolute zero!\n')

    return round(celsius, 2)


def fahrenheit_to_kelvin(fahrenheit):

    kelvin = ((fahrenheit - 32) / 1.80)+ 273.15
    if fahrenheit < -459.67:
        raise Exception('Cannot be below absolute zero!\n')

    return round(kelvin, 2)


def kelvin_to_fahrenheit(kelvin):

    fahrenheit = (kelvin - 273.15) * 1.80 + 32

    return round(fahrenheit, 2)


# Display the available unit conversions, prompt the user to choose
def temp_choices():

    print()

    for key, val in temp_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a temperature conversion: '))
    print()

    if conversion == 1:
        user_fahrenheit = float(input('Enter an amount in fahrenheit to be converted to celsius: '))
        print(f'{user_fahrenheit} degrees F equals {fahrenheit_to_celsius(user_fahrenheit)} degrees C.')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 2:
        user_celsius = float(input('Enter an amount in celsius to be converted to fahrenheit: '))
        print(f'{user_celsius} degrees C equals {celsius_to_fahrenheit(user_celsius)} degrees F.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 3:
        user_celsius = float(input('Enter an amount in celsius to be converted to Kelvin: '))
        print(f'{user_celsius} degrees C equals {celsius_to_kelvin} K.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 4:
        user_kelvin = float(input('Enter an amount in Kelvin to be converted to celsius: '))
        print(f'{user_kelvin} degrees K equals {kelvin_to_celsius(user_kelvin)} degrees C.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 5:
        user_fahrenheit = float(input('Enter an amount in fahrenheit to be converted to Kelvin: '))
        print(f'{user_fahrenheit} degrees F equals {fahrenheit_to_kelvin(user_fahrenheit)} degrees K.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 6:
        user_kelvin = float(input('Enter an amount in fahrenheit to be converted to Kelvin: '))
        print(f'{user_kelvin} degrees K equals {kelvin_to_fahrenheit(user_kelvin)} degrees F.\n')
        input("Conversion complete. Press enter to exit.")
    else:
        raise Exception('Invalid value entered.\n')