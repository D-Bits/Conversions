
def meters_to_planck_lengths():

    meters = float(input('Enter an amount of meters to be converted into Planck Lengths: '))
    conversion = 1.16 * 10**-34
    planck_lengths = meters * conversion

    print(round(planck_lengths, 2))
