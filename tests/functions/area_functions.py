"""
A list of parameterized area conversions,
for unit testing purposes
"""

def acres_to_sqft(acres):

    sqft = acres * 43560

    return round(sqft, 2)


def sqft_to_acres(sqft):

    acres = sqft / 43560

    return round(acres, 2)


def acres_to_hectares(acres):

    hectares = acres / 2.4711

    return round(hectares, 2)


def hectares_to_acres(hectares):

    acres = hectares * 2.4711

    return round(acres, 2)
