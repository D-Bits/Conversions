"""
A list of parameterized length conversions,
for unit testing purposes
"""

def feet_to_meters(feet):

    meters = feet / 3.2808

    return round(meters, 2)


def meters_to_feet(meters):

    feet = meters * 3.2808

    return round(feet, 2)


def miles_to_kilos(miles):

    kilos = miles / 0.62137

    return round(kilos, 2)


def kilos_to_miles(kilos):

    miles = kilos * 0.62137

    return round(miles, 2)
