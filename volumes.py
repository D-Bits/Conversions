
volume_options = {
    '1': 'Litres to Gallons',
    '2': 'Gallons to Litres'
}


def litres_to_gallons():

    litres = float(input('Enter an amount in litres to be converted into gallons: '))
    if litres == 0:
        raise Exception('Cannot calculate zero value!\n')
    gallons = litres * 0.26417
    rounded = round(gallons, 2)

    print(f'{litres} L equals {rounded} gal.\n')


def gallons_to_litres():

    gallons = float(input('Enter an amount in gallons to be converted into litres: '))
    if gallons == 0:
        raise Exception('Cannot calculate zero value!\n')
    litres = gallons / 0.26417
    rounded = round(litres, 2)

    print(f'{gallons} gal equals {rounded} L.\n')


# Display the available unit conversions, prompt the user to choose
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
        raise Exception('Invalid value entered.\n')