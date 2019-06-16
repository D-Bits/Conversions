"""
A list of parameterized temperature conversions,
for unit testing purposes
"""


def pounds_to_kilograms(pounds):

    kilos = pounds / 2.2046

    return round(kilos, 2)


def kilograms_to_pounds(kilos):

    pounds = kilos * 2.2046

    return round(pounds, 2)