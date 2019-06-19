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

def rems_to_sieverts(rems):

    sieverts = rems / 100

    return round(sieverts, 2)


def sieverts_to_rems(sieverts):

    rems = sieverts * 100

    return round(rems, 2)


def rads_to_grays(rads):

    grays = rads /100

    return round(grays, 2) 
    

def grays_to_rads(grays):

    rads = grays * 100

    return round(rads, 2)


def dosimetry_choices():

    print()

    for key, val in dosimetry_options.items():

        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a dosimetry conversion: '))

    if conversion == 1:
        user_rems = float(input('Enter an amount of Roentigen Equivalent Mans (rems) to be converted to Sieverts: '))
        print(f'{user_rems} rems equals {rems_to_sieverts(user_rems)} Sv.\n')
    elif conversion == 2:
        user_sv = float(input('Enter an amount of Sieverts to be converted to Roentigen Equivalent Mans (rems): '))
        print(f'{user_sv} Sv equals {sieverts_to_rems(user_sv)} rems.\n')
    elif conversion == 3:
        user_rads = float(input('Enter an amount of rads to be converted to grays: '))
        print(f'{user_rads} rads equals {rads_to_grays(user_rads)} grays.\n')
    elif conversion == 4:
        user_grays = float(input('Enter an amount of grays to be converted to rads: '))
        print(f'{user_grays} grays equals {grays_to_rads(user_grays)} rads.\n')
    else:
        raise Exception('Invalid value entered.\n')