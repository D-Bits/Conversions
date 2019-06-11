""" 
A collection of functions to do conversions for 
measurements of ionizing radiation (REMS, Sieverts, etc)
"""

def rems_to_sieverts():

    rems = float(input('Enter an amount of Roentigen Equivalent Mans (rems) to be converted to Sieverts: '))
    sieverts = rems / 100

    print(round(sieverts, 2))


def sieverts_to_rems():

    sieverts = float(input('Enter an amount of Sieverts to be converted to Roentigen Equivalent Mans (rems): '))
    rems = sieverts * 100

    print(round(rems, 2))
