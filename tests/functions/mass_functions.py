"""
A list of parameterized mass conversions,
for unit testing purposes
"""


def pounds_to_kilograms(pounds):

    kilos = pounds / 2.2046

    return round(kilos, 2)


def kilograms_to_pounds(kilos):

    pounds = kilos * 2.2046

    return round(pounds, 2)


def ounces_to_grams(ounces):

    grams = (ounces / 0.035274)

    return grams


def grams_to_ounces(grams):

    ounces = grams * 0.035274

    return ounces