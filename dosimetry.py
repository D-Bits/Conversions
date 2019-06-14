""" 
A collection of functions to do conversions for 
measurements of ionizing radiation (Rems, Sieverts, etc)
"""

dosimetry_options = {
    '1': 'Rems to Sieverts',
    '2': 'Sieverts to Rems',
    '3': 'Rads to Grays'
}

# Rems and Sieverts both measure doseage equivalents
def rems_to_sieverts():

    rems = float(input('Enter an amount of Roentigen Equivalent Mans (rems) to be converted to Sieverts: '))
    sieverts = rems / 100
    rounded = round(sieverts, 2)

    print(f'{rems} rems equals {rounded} Sv.')


def sieverts_to_rems():

    sieverts = float(input('Enter an amount of Sieverts to be converted to Roentigen Equivalent Mans (rems): '))
    rems = sieverts * 100
    rounded = round(rems, 2)

    print(f'{sieverts} Sv equals {rounded} rems.')


# Grays and rads measure Absorbed doses
def rads_to_grays():

    rads = float(input('Enter an amount of rads to be converted to grays: '))
    grays = rads / 100
    rounded = round(grays, 2)

    print(f'{rads} rads equals {rounded} grays.')


def rads_to_grays():

    grays = float(input('Enter an amount of grays to be converted to rads: '))
    rads = grays * 100
    rounded = round(rads, 2)

    print(f'{grays} grays equals {rounded} rads.')


# Display the available unit conversions, prompt the user to choose
def dosimetry_choices():

    print()

    for key, val in dosimetry_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a dosimetry conversion: '))
    print()

    if conversion == 1:
        rems_to_sieverts()
    elif conversion == 2:
        sieverts_to_rems()
    elif conversion == 3:
        rads_to_grays()
    else:
        raise Exception('Invalid value entered.')