""" 
Conversions for metric, imperial, and various astronomical
measuring units (AU, light years, parsecs).
"""

astro_options = {
    '1': 'Kilometers to AU',
    '2': 'AU to Kilometers',
    '3': 'Miles to AU',
    '4': 'AU to Miles',
    '5': 'Kilometers to Light Years',
    '6': 'Light Years to Kilometers',
    '7': 'Miles to Light Years',
    '8': 'Light Years to Miles',
    '9': 'Parsecs to Light Years',
    '10': 'Light Years to Parsecs'
}


def kilometers_to_au():

    kilos = float(input('Enter an amount in kilometers to be converted to astronomical units (AU): '))
    if kilos == 0:
        raise Exception('Cannot calculate zero value!')
    au = kilos / 149597900
    rounded = round(au, 2)

    print(f'{kilos} kms equals {rounded} AU.')


def au_to_kilometers():

    au = float(input('Enter an amount in astronomical units (AU) to be converted to kilometers: '))
    if au == 0:
        raise Exception('Cannot calculate zero value!')
    kilos = au * 149597900
    rounded = round(kilos, 2)

    print(f'{au} AU equals {rounded} kms.')


def miles_to_au():

    miles = float(input('Enter an amount in miles to be converted to astronomical units (AU): '))
    if miles == 0:
        raise Exception('Cannot calculate zero value!')
    au = miles / 92955825.9
    rounded = round(au, 2)

    print(f'{miles} miles equals {rounded} AU')


def au_to_miles():

    au = float(input('Enter an amount in astronomical units (AU) to be converted to miles: '))
    if au == 0:
        raise Exception('Cannot calculate zero value!')
    miles = au * 92955825.9
    rounded = round(miles, 2)

    print(f'{au} AU equals {miles} mi.')


def kilometers_to_ly():

    kilos = float(input('Enter an amount in kilometers to be converted to light years (LY): '))
    if kilos == 0:
        raise Exception('Cannot calculate zero value!')
    ly = kilos / 9460730000000
    rounded = round(ly, 2)

    print(f'{kilos} kms equals {rounded} lys.')


def ly_to_kilometers():

    ly = float(input('Enter an amount in light years (LY) to be converted to kilometers: '))
    if ly == 0:
        raise Exception('Cannot calculate zero value!')
    kilos = ly * 9460730000000
    rounded = round(kilos, 2)

    print(f'{ly} ly equals {rounded} kms.')


def miles_to_ly():

    miles = float(input('Enter an amount in miles to be converted to light years (LY): '))
    if miles == 0:
        raise Exception('Cannot calculate zero value!')
    ly= miles / 5878625000000
    rounded = round(ly, 2)

    print(f'{miles} mi equals {rounded} ly')


def ly_to_miles():

    ly = float(input('Enter an amount in light years to be converted to miles: '))
    if ly == 0:
        raise Exception('Cannot calculate zero value!')
    miles = ly * 5878625000000
    rounded = round(miles, 2)

    print(f'{ly} ly equals {rounded} mi.')


def parsecs_to_ly():

    parsecs = float(input('Enter an amount in parsecs to be converted to light years: '))
    if parsecs == 0:
        raise Exception('Cannot calculate zero value!')
    ly = parsecs * 3.26156
    rounded = round(ly, 2)

    print(round(ly, 2))


def ly_to_parsecs():

    ly = float(input('Enter an amount in light years to be converted to parsecs: '))
    if ly == 0:
        raise Exception('Cannot calculate zero value!')
    parsecs = ly / 3.26156

    print(round(parsecs, 2))


# Display the available unit conversions, prompt the user to choose
def astro_choices():

    print()

    for key, val in astro_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a astronomical conversion: '))
    print()

    if conversion == 1:
        kilometers_to_au()
    elif conversion == 2:
        au_to_kilometers()
    elif conversion == 3:
        miles_to_au()
    elif conversion == 4:
        au_to_miles()
    elif conversion == 5:
        kilometers_to_ly()
    elif conversion == 6:
        ly_to_kilometers()
    elif conversion == 7:
        miles_to_ly()
    elif conversion == 8:
        ly_to_miles()
    elif conversion == 9:
        parsecs_to_ly()
    elif conversion == 10:
        ly_to_parsecs()
    else:
        raise Exception('Invalid value entered.')