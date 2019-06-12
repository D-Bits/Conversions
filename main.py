from temperature import temp_choices
from lengths import length_choices
from mass import mass_choices
from dosimetry import dosimetry_choices
from astronomy import astro_choices
from volumes import volume_choices


options = {
    '1': 'Temperature Conversions',
    '2': 'Mass Conversions',
    '3': 'Length Conversions',
    '4': 'Volume Conversions',
    '5': 'Dosimetry Conversions',
    '6': 'Astronomical Conversions'
}


if __name__ == "__main__":
    
    print()

    for key, val in options.items():
        
        print(key, val)

    print()
    conversion = int(input('Enter one of the above integers to specify a category: '))
    print()

    if conversion == 1:
        temp_choices()
    elif conversion == 2:
        mass_choices()
    elif conversion == 3:
        length_choices()
    elif conversion == 4:
        volume_choices()
    elif conversion == 5:
        dosimetry_choices()
    elif conversion == 6:
        astro_choices()
    else:
        raise Exception('Invalid value entered.')