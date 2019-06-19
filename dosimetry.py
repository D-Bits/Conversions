""" 
A collection of functions to do conversions for 
measurements of ionizing radiation (Rems, Sieverts, etc)
"""

dosimetry_options = {
    '1': 'Rems to Sieverts',
    '2': 'Sieverts to Rems',
    '3': 'Rads to Grays',
    '4': 'Grays to Rads'
}

# Rems and Sieverts both measure doseage equivalents
def rems_to_sieverts():

    rems = float(input('Enter an amount of Roentigen Equivalent Mans (rems) to be converted to Sieverts: '))
    if rems == 0:
        raise Exception('Cannot calculate zero value!\n')
    sieverts = rems / 100
    rounded = round(sieverts, 2)

    print(f'{rems} rems equals {rounded} Sv.\n')


def sieverts_to_rems():

    sieverts = float(input('Enter an amount of Sieverts to be converted to Roentigen Equivalent Mans (rems): '))
    if sieverts == 0:
        raise Exception('Cannot calculate zero value!')
    rems = sieverts * 100
    rounded = round(rems, 2)

    print(f'{sieverts} Sv equals {rounded} rems.\n')


# Grays and rads measure Absorbed doses
def rads_to_grays():

    rads = float(input('Enter an amount of rads to be converted to grays: '))
    if rads == 0:
        raise Exception('Cannot calculate zero value!\n')
    grays = rads / 100
    rounded = round(grays, 2)

    print(f'{rads} rads equals {rounded} grays.\n')


def grays_to_rads():

    grays = float(input('Enter an amount of grays to be converted to rads: '))
    if grays == 0:
        raise Exception('Cannot calculate zero value!\n')
    rads = grays * 100
    rounded = round(rads, 2)

    print(f'{grays} grays equals {rounded} rads.\n')


# Display the available unit conversions, prompt the user to choose
def dosimetry_choices():

    print()

    for key, val in dosimetry_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a dosimetry conversion: '))

    if conversion == 1:
        rems_to_sieverts()
    elif conversion == 2:
        sieverts_to_rems()
    elif conversion == 3:
        rads_to_grays()
    elif conversion == 4:
        grays_to_rads()
    else:
        raise Exception('Invalid value entered.\n')