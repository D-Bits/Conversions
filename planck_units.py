"""
Conversions for Planck units to metric units.
"""

planck_options ={
    '1': 'Meters to Planck lengths.',
    '2': 'Planck lengths to meters.'
}


def meters_to_planck_lengths(meters): 

    conversion = 1.61605 * 10**-35
    planck_lengths = meters / conversion
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')

    return planck_lengths


def planck_lengths_to_meters(pl):

    conversion = 1.61605 * 10**-35
    meters = pl * conversion
    if pl == 0:
        raise Exception('Cannot calculate zero value!\n')

    return meters


# Display availble conversion options, and prompt the user to choose
def planck_choices():

    print()

    for key, val in planck_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a Planck unit conversion: '))
    print()

    if conversion == 1:
        user_meters = float(input('Enter an amount of meters to be converted into Planck Lengths: '))
        print(f'{user_meters} meters equals {meters_to_planck_lengths(user_meters)} Planck lengths.\n')
    elif conversion == 2:
        user_lp = float(input('Enter an amount of Planck lengths to be converted into meters: '))
        print(f'{user_lp} Planck lengths equals {planck_lengths_to_meters(user_lp)} meters.\n')
    else:
        raise Exception('Invalid value entered.')