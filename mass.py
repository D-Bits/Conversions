
mass_options = {
    '1': 'Pounds to Kilograms',
    '2': 'Kilograms to Pounds'
}


def pounds_to_kilograms():

    pounds = float(input('Enter an amount in pounds to be converted to kilos: '))
    kilos = pounds / 2.2046

    print(round(kilos, 2))


def kilograms_to_pounds():

    kilos = float(input('Enter an amount in pounds to be converted to kilos: '))
    pounds = kilos * 2.2046

    print(round(pounds, 2))


def mass_choices():

    print()

    for key, val in mass_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a mass conversion: '))
    print()

    if conversion == 1:
        pounds_to_kilograms()
    elif conversion == 2:
        kilograms_to_pounds()
    else:
        raise Exception('Invalid value entered.')