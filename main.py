from temperature import(
    temp_choices,
    fahrenheit_to_celsius, 
    celsius_to_fahrenheit, 
    celsius_to_kelvin, 
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit
)
from lengths import( 
    feet_to_meters, 
    meters_to_feet, 
    miles_to_kilometers, 
    kilometers_to_miles,
    length_choices
)
from mass import(
    pounds_to_kilograms,
    kilograms_to_pounds,
    mass_choices
)
from dosimetry import(
    rems_to_sieverts,
    sieverts_to_rems,
    dosimetry_choices
)

options = {
    '1': 'Temperature Conversions',
    '2': 'Mass Conversions',
    '3': 'Length Conversions',
    '4': 'Dosimetry Conversions'
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
        dosimetry_choices()
    else:
        raise Exception('Invalid value entered.')