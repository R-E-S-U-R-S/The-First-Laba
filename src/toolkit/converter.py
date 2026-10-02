from asyncio import constants

from errors import unknown_conversion_type
from errors import unknown_conversion_units

lenght_cnostants={
    "meters": 1,
    "kilometers": 1000,
    "millimeters": 0.001,
    "santimeters": 0.01
}

mass_constants={
    "killogramm": 1000,
    "gramm": 1,
    "milligramm": 0.01,
    "ton": 1000000
}

def lenght_converter(inpt_lenght:float, inpt_units:str, output_units:str)->float:
    if inpt_units not in lenght_cnostants or output_units not in lenght_cnostants:
        return unknown_conversion_units()
    inpt_lenght*=lenght_cnostants[inpt_units]
    return inpt_lenght/lenght_cnostants[output_units]

def mass_converter(inpt_mass:float, inpt_units:str, output_units:str)->float:
    inpt_mass*=mass_constants[inpt_units]
    if inpt_units not in mass_constants or output_units not in mass_constants:
        return unknown_conversion_units()
    return inpt_mass/mass_constants[output_units]


def converter(convertion_unit_type):
    if convertion_unit_type.lower()=="mass":
        print(mass_converter(input("").split()))
    elif convertion_unit_type.lower()=='lenght':
        print(lenght_converter(input("").split()))
    else:
        return unknown_conversion_type()

converter(input("unit type "))