"""
Conversions for Planck units to metric units.
"""

planck_options ={
    '1': 'Meters to Planck lengths.',
    '2': 'Planck lengths to meters.',
    '3': 'Light years to Planck Lengths.'
}


def meters_to_planck_lengths():

    meters = float(input('Enter an amount of meters to be converted into Planck Lengths: '))
    conversion = 1.61605 * 10**-35
    planck_lengths = meters / conversion
    rounded = round(planck_lengths, 2)

    print(f'{meters} meters equals {rounded} Planck lengths.\n')


def planck_lengths_to_meters():

    pl = float(input('Enter an amount of Planck lengths to be converted into meters: '))
    conversion = 1.61605 * 10**-35
    meters = pl * conversion

    print(f'{pl} Planck lengths equals {meters} meters.\n')


# Light years to Planck lengths 
def ly_to_pl():

    ly = float(input('Enter an amount of light years to be converted to Planck lengths: '))
    conversion = (1.61605 * 10**-35) * 9460730000000000
    plankc_lengths = conversion * ly

    print(f'{ly} ly equals {plankc_lengths} Planck lengths.')


# Display availble conversion options, and prompt the user to choose
def planck_choices():

    print()

    for key, val in planck_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a Planck unit conversion: '))
    print()

    if conversion == 1:
        meters_to_planck_lengths()
    elif conversion == 2:
        planck_lengths_to_meters()
    elif conversion == 3:
        ly_to_pl()
    else:
        raise Exception('Invalid value entered.')