"""
A list of parameterized dosimetry conversions,
for unit testing purposes.
"""


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

    return round(grays, 2)