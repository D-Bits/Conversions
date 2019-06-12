
volume_options = {
    '1': 'Litres to Gallons',
    '2': 'Gallons to Litres'
}


def litres_to_gallons():

    litres = float(input('Enter an amount in litres to be converted into gallons: '))
    gallons = litres * 0.26417
    rounded = round(gallons, 2)

    print(f'{litres} L equals {rounded} gal.')


def gallons_to_litres():

    gallons = float(input('Enter an amount in gallons to be converted into litres: '))
    litres = gallons / 0.26417
    rounded = round(litres, 2)

    print(f'{gallons} gal equals {rounded} L.')


def volume_choices():

    print()

    for key, val in volume_options.items():
        
        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a volume conversion: '))
    print()

    if conversion == 1:
        litres_to_gallons()
    elif conversion == 2:
        gallons_to_litres()
    else:
        raise Exception('Invalid value entered.')