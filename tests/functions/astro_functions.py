"""
A list of parameterized astronomical conversions,
for unit testing purposes.
"""

def kilometers_to_au(kilos):

    au = kilos / 149597900

    return round(au, 2)


def au_to_kilometers(au):

    kilos = au * 149597900

    return round(kilos, 2)


def miles_to_au(miles):

    au = miles / 92955825.9

    return round(au, 2)


def au_to_miles(au):

    miles = au * 92955825.9

    return round(miles, 2)


def kilometers_to_ly(kilos):

    ly = kilos / 9460730000000

    return round(ly, 2)


def ly_to_kilometers(ly):

    kilos = ly * 9460730000000

    return round(kilos, 2)


def miles_to_ly(miles):

    ly= miles / 5878625000000

    return round(ly, 2)


def ly_to_miles(ly):

    miles = ly * 5878625000000

    return round(miles, 2)


def parsecs_to_ly(parsecs):

    ly = parsecs *  3.26156

    return round(ly, 2)


def ly_to_parsecs(ly):

    parsecs = ly /  3.26156

    return parsecs