
length_options = {
    '1': 'Feet to Meters',
    '2': 'Meters to Feet',
    '3': 'Miles to Kilometers',
    '4': 'Kilometers to Miles'
}

def feet_to_meters():

    feet = float(input('Enter an amount of feet to be converted into meters: '))
    if feet == 0:
        raise Exception('Cannot calculate zero value!')
    meters = feet / 3.2808
    rounded = round(meters, 2)

    print(f'{feet} ft equals {rounded} m.')


def meters_to_feet():

    meters = float(input('Enter an amount of meters to be converted into feet: '))
    if meters == 0:
        raise Exception('Cannot calculate zero value!')
    feet = meters * 3.2808
    rounded = round(feet, 2)

    print(f'{meters} m equals {rounded} ft.')


def miles_to_kilometers():

    miles = float(input('Enter an amount of miles to be converted to kilometers: '))
    if miles == 0:
        raise Exception('Cannot calculate zero value!')
    kilometers = miles / 0.62137
    rounded = round(kilometers, 2)

    print(f'{miles} mi equals {rounded} kms.')


def kilometers_to_miles():

    kilos = float(input('Enter an amount of kilometers to be converted to miles: '))
    if kilos == 0:
        raise Exception('Cannot calculate zero value!')
    miles = kilos * 0.62137
    rounded = round(miles, 2)

    print(f'{kilos} kms equals {rounded} mi.')


# Display the available unit conversions, prompt the user to choose
def length_choices():

    print()

    for key, val in length_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a length conversion: '))
    print()

    if conversion == 1:
        feet_to_meters()
    elif conversion == 2:
        meters_to_feet()
    elif conversion == 3:
        miles_to_kilometers()
    elif conversion == 4:
        kilometers_to_miles()
    else:
        raise Exception('Invalid value entered.')