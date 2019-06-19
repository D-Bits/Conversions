from temperature import temp_choices
from lengths import length_choices
from mass import mass_choices
from dosimetry import dosimetry_choices
from astronomy import astro_choices
from area import area_choices
from volumes import volume_choices
from planck_units import planck_choices


# Conversion options
options = {
    '1': 'Temperature Conversions',
    '2': 'Mass Conversions',
    '3': 'Length Conversions',
    '4': 'Volume Conversions',
    '5': 'Area Conversions',
    '6': 'Dosimetry Conversions',
    '7': 'Astronomical Conversions',
    '8': 'Planck Unit Conversions'
}


if __name__ == "__main__":
    
    print()

    for key, val in options.items():
        
        print(key, val)

    print() # Prompt the user to choose a unit conversion category
    conversion = int(input('Enter one of the above integers to specify a category: '))

    if conversion == 1:
        temp_choices()
    elif conversion == 2:
        mass_choices()
    elif conversion == 3:
        length_choices()
    elif conversion == 4:
        volume_choices()
    elif conversion == 5:
        area_choices()
    elif conversion == 6:
        dosimetry_choices()
    elif conversion == 7:
        astro_choices()
    elif conversion == 8:
        planck_choices()
    else:
        raise Exception('Invalid value entered.')