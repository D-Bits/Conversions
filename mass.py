
mass_options = {
    '1': 'Pounds to Kilograms',
    '2': 'Kilograms to Pounds',
    '3': 'Ounces to Grams.'
}


def pounds_to_kilograms():

    pounds = float(input('Enter an amount in pounds to be converted to kilos: '))
    if pounds == 0:
        raise Exception('Cannot calculate zero value!')
    kilos = pounds / 2.2046
    rounded = round(kilos, 2)

    print(f'{pounds} lbs equals {rounded} kgs.')


def kilograms_to_pounds():

    kilos = float(input('Enter an amount in kilograms to be converted to pounds: '))
    if kilos == 0:
        raise Exception('Cannot calculate zero value!')
    pounds = kilos * 2.2046
    rounded = round(pounds, 2)

    print(f'{kilos} kgs equals {rounded} lbs.')


def ounces_to_grams():

    ounces = float(input('Enter an amount in ounces to be converted to grams: '))
    if ounces == 0:
        raise Exception('Cannot calculate zero value!\n')
    grams = ounces / 0.035274
    rounded = round(grams, 2)
    
    print(f'{ounces} oz. equals {rounded} g.\n')


def grams_to_ounces():

    grams = float(input('Enter an amount in grams to be converted to ounces: '))
    if grams == 0:
        raise Exception('Cannot calculate zero value!\n')
    ounces = grams * 0.035274
    rounded = round(grams, 2)
    
    print(f'{grams} g. equals {rounded} oz.\n')


# Display the available unit conversions, prompt the user to choose
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
    elif conversion == 3:
        ounces_to_grams()
    elif conversion == 4:
        grams_to_ounces()
    else:
        raise Exception('Invalid value entered.\n')