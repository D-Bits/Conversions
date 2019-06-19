
area_options = {
    '1': 'Acres to Sq. Feet.',
    '2': 'Sq. Feet to Acres.',
    '3': 'Acres to Hectares',
    '4': 'Hectares to Acres'
}


def acres_to_sqft():

    acres = float(input('Enter an amount in acres to be converted into sq. ft.: '))
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')
    sqft = acres * 43560
    rounded = round(sqft, 2)

    print(f'{acres} ac equals {rounded} sq. ft.\n')


def sqft_to_acres():

    sqft = float(input('Enter an amount in sq. ft. to be converted into acres: '))
    if sqft == 0:
        raise Exception('Cannot calculate zero value!\n')
    acres = sqft / 43560
    rounded = round(acres, 2)

    print(f'{sqft} sq. ft equals {rounded} acres.\n')


def acres_to_hectares():

    acres = float(input('Enter an amount in acres to be converted into hectares: '))
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')
    hectares = acres / 2.4711
    rounded = round(hectares, 2)

    print(f'{acres} ac equals {rounded} ha.\n')


def hectares_to_acres():

    hectares = float(input('Enter an amount in hectares to be converted into acres: '))
    if hectares == 0:
        raise Exception('Cannot calculate zero value!\n')
    acres = hectares * 2.4711
    rounded = round(acres, 2)

    print(f'{hectares} ha equals {rounded} ac.\n')


def area_choices():

    print()

    for key, val in area_options.items():
        
        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify an area conversion: '))
    print()

    if conversion == 1:
        acres_to_sqft()
    elif conversion == 2:
        sqft_to_acres()
    elif conversion == 3:
        acres_to_hectares()
    elif conversion == 4:
        hectares_to_acres()
    else:
        raise Exception('Invalid value entered.\n')