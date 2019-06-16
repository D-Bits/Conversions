"""
A list of parameterized volumne conversions,
for unit testing purposes
"""

def litres_to_gallons(litres):

    gallons = litres * 0.26417

    return round(gallons, 2)


def gallons_to_litres(gallons):

    litres = gallons / 0.26417

    return round(litres, 2)