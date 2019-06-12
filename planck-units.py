
def meters_to_planck_lengths():

    meters = float(input('Enter an amount of meters to be converted into Planck Lengths: '))
    conversion = 1.16 * 10**-34
    planck_lengths = meters / conversion
    rounded = round(planck_lengths, 2)

    print(f'{meters} meters equals {rounded} Planck lengths.')

