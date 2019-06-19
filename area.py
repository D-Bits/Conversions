
# Choices for users
area_options = {
    '1': 'Acres to Sq. Feet.',
    '2': 'Sq. Feet to Acres.',
    '3': 'Acres to Hectares',
    '4': 'Hectares to Acres'
}


def acres_to_sqft(acres):

    sqft = acres * 43560
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(sqft, 2)


def sqft_to_acres(sqft):

    acres = sqft / 43560
    if sqft == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(acres, 2)


def acres_to_hectares(acres):

    hectares = acres / 2.4711
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(hectares, 2)


def hectares_to_acres(hectares):

    acres = hectares * 2.4711
    if hectares == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(acres, 2)


def area_choices():

    print()

    for key, val in area_options.items():
        
        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify an area conversion: '))
    print()

    if conversion == 1:
        user_acres = float(input('Enter an amount in acres to be converted into sq. ft.: '))
        print(f'{user_acres} ac equals {acres_to_sqft(user_acres)} sq. ft.\n')
    elif conversion == 2:
        user_sqft = float(input('Enter an amount in sq. ft. to be converted into acres: '))
        print(f'{user_sqft} sq. ft equals {sqft_to_acres(user_sqft)} acres.\n')
    elif conversion == 3:
        user_acres = float(input('Enter an amount in acres to be converted into hectares: '))
        print(f'{user_acres} sq. ft equals {acres_to_hectares(user_acres)} acres.\n')
    elif conversion == 4:
        user_hectares = float(input('Enter an amount in hectares to be converted into acres: '))
        print(f'{user_hectares} ha equals {hectares_to_acres(user_hectares)} ac.\n')
    else:
        raise Exception('Invalid value entered.\n')