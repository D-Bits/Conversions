"""
A list of parameterized Planck unit conversions,
for unit testing purposes.
"""


def meters_to_planck_lengths(meters): 

    conversion = 1.61605 * 10**-35
    planck_lengths = meters / conversion

    return planck_lengths


def planck_lengths_to_meters(pl):

    conversion = 1.61605 * 10**-35
    meters = pl * conversion

    return meters