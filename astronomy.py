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
    au = kilos / 149597900

    print(round(au, 2))


def au_to_kilometers():

    au = float(input('Enter an amount in astronomical units (AU) to be converted to kilometers: '))
    kilos = au * 149597900

    print(round(kilos, 2))


def miles_to_au():

    miles = float(input('Enter an amount in miles to be converted to astronomical units (AU): '))
    au = miles / 92955825.9

    print(round(au, 2))


def au_to_miles():

    au = float(input('Enter an amount in astronomical units (AU) to be converted to miles: '))
    miles = au * 92955825.9

    print(round(miles, 2))


def kilometers_to_ly():

    kilos = float(input('Enter an amount in kilometers to be converted to light years (LY): '))
    ly = kilos / 9460730000000

    print(round(ly, 2))


def ly_to_kilometers():

    ly = float(input('Enter an amount in kilometers to be converted to light years (LY): '))
    kilos = ly * 9460730000000


def miles_to_ly():

    miles = float(input('Enter an amount in miles to be converted to light years (LY): '))
    ly= miles / 5878625000000

    print(round(ly, 2))


def ly_to_miles():

    ly = float(input('Enter an amount in light years to be converted to miles: '))
    miles= ly * 5878625000000

    print(round(ly, 2))


def parsecs_to_ly():

    parsecs = float(input('Enter an amount in parsecs to be converted to light years: '))
    ly = parsecs * 3.26

    print(round(ly, 2))


def ly_to_parsecs():

    ly = float(input('Enter an amount in light years to be converted to parsecs: '))
    parsecs = ly / 3.26

    print(round(parsecs, 2))


def astro_choices():

    print()

    for key, val in astro_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a length conversion: '))
    print()

    if conversion == 1:
        kilometers_to_au
    elif conversion == 2:
        au_to_kilometers
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