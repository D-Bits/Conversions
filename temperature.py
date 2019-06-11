

def fahrenheit_to_celsius():

    fahrenheit = float(input('Enter an amount in fahrenheit to be converted to celsius: '))
    celsius = fahrenheit - 32 / 1.80

    print(round(celsius, 2))


def celsius_to_fahrenheit():

    celsius = float(input('Enter an amount in celsius to be converted to fahrenheit: '))
    fahrenheit = celsius * 1.80 + 32.00

    print(round(fahrenheit, 2))
    

def celsius_to_kelvin():
    
    celsius = float(input('Enter an amount in celsius to be converted to Kelvin: '))
    kelvin = celsius + 273.15

    print(round(kelvin, 2))


def kelvin_to_celsius():
    
    kelvin = float(input('Enter an amount in Kelvin to be converted to celsius: '))
    celsius = kelvin - 273.15

    print(round(celsius, 2))


def fahrenheit_to_kelvin():

    fahrenheit = float(input('Enter an amount in Kelvin to be converted to fahrenheit: '))
    kelvin = fahrenheit - 32 / 1.80 + 273.15

    print(round(kelvin, 2))


def kelvin_to_fahrenheit():

    kelvin = float(input('Enter an amount in fahrenheit to be converted to Kelvin: '))
    fahrenheit = (kelvin - 273.15) * 1.80 + 32

    print(round(fahrenheit, 2))

