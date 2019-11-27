
volume_options = {
    '1': 'Litres to Gallons',
    '2': 'Gallons to Litres'
}


def litres_to_gallons(litres):

    gallons = litres * 0.26417
    if litres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(gallons, 2)


def gallons_to_litres(gallons):

    litres = gallons / 0.26417
    if gallons == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(litres, 2)


# Display the available unit conversions, prompt the user to choose
def volume_choices():
 
    print()

    for key, val in volume_options.items():
        
        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a volume conversion: '))
    print()

    if conversion == 1:
        user_litres = float(input('Enter an amount in litres to be converted into gallons: '))
        print(f'{user_litres} L equals {litres_to_gallons(user_litres)} gal.\n')
        input("Conversion complete. Press enter to exit.")
    elif conversion == 2:
        user_gal = float(input('Enter an amount in gallons to be converted into litres: '))
        print(f'{user_gal} gal equals {gallons_to_litres(user_gal)} L.\n')
        input("Conversion complete. Press enter to exit.")
    else:
        raise Exception('Invalid value entered.\n')