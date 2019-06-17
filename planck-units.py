
def meters_to_planck_lengths():

    meters = float(input('Enter an amount of meters to be converted into Planck Lengths: '))
    conversion = 1.61605 * 10**-35
    planck_lengths = meters / conversion
    rounded = round(planck_lengths, 2)

    print(f'{meters} meters equals {rounded} Planck lengths.')


def planck_lengths_to_meters():

    pl = float(input('Enter an amount of Planck lengths to be converted into meters: '))
    conversion = 1.61605 * 10**-35
    meters = pl * conversion

    print(f'{pl} Planck lengths equals {meters} meters.')

