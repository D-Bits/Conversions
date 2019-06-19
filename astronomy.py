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


def kilometers_to_au(kilos):

    au = kilos / 149597900
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(au, 2)


def au_to_kilometers(au):

    kilos = au * 149597900
    if au == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def miles_to_au(miles):

    au = miles / 92955825.9
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(au, 2)


def au_to_miles(au):

    miles = au * 92955825.9
    if au == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(miles, 2)


def kilometers_to_ly(kilos):

    ly = kilos / 9460730000000

    return round(ly, 2)


def ly_to_kilometers(ly):

    kilos = ly * 9460730000000

    return round(kilos, 2)


def miles_to_ly(miles):

    ly= miles / 5878625000000

    return round(ly, 2)


def ly_to_miles(ly):

    miles = ly * 5878625000000

    return round(miles, 2)


def parsecs_to_ly(parsecs):

    ly = parsecs *  3.26156

    return round(ly, 2)


def ly_to_parsecs(ly):

    parsecs = ly /  3.26156

    return parsecs


def astro_choices():

    print()

    for key, val in astro_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a astronomical conversion: '))

    if conversion == 1:
        user_kilos = float(input('Enter an amount in kilometers to be converted to astronomical units (AU): '))
        print(f'{user_kilos} kms equals {kilometers_to_au(user_kilos)} AU.\n')
    elif conversion == 2:
        user_au = float(input('Enter an amount in astronomical units (AU) to be converted to kilometers: '))
        print(f'{user_au} AU equals {au_to_kilometers(user_au)} kms.\n')
    elif conversion == 3:
        user_miles = float(input('Enter an amount in miles to be converted to astronomical units (AU): '))
        print(f'{user_miles} miles equals {miles_to_au(user_miles)} AU\n')
    elif conversion == 4:
        user_au = float(input('Enter an amount in astronomical units (AU) to be converted to miles: '))
        print(f'{user_au} AU equals {au_to_miles(user_au)} mi.\n')
    elif conversion == 5:
        user_kilos = float(input('Enter an amount in kilometers to be converted to light years (LY): '))
        print(f'{user_kilos} kms equals {kilometers_to_ly(user_kilos)} lys.\n')
    elif conversion == 6:
        user_ly = float(input('Enter an amount in light years (LY) to be converted to kilometers: '))
        print(f'{user_ly} ly equals {ly_to_kilometers(user_ly)} kms.\n')
    elif conversion == 7:
        user_miles = float(input('Enter an amount in miles to be converted to light years (LY): '))
        print(f'{user_miles} mi equals {miles_to_ly(user_miles)} ly \n')
    elif conversion == 8:
        user_ly = float(input('Enter an amount in light years to be converted to miles: '))
        print(f'{user_ly} ly equals {ly_to_miles(user_ly)} mi.\n')
    elif conversion == 9:
        user_pc = float(input('Enter an amount in parsecs to be converted to light years: '))
        print(f'{user_pc} pc equals {parsecs_to_ly(user_pc)} ly.\n')
    elif conversion == 10:
        user_ly = float(input('Enter an amount in light years to be converted to parsecs: '))
        print(f'{user_ly} ly equals {ly_to_parsecs(user_ly)} pc.\n')
    else:
        raise Exception('Invalid value entered.\n')