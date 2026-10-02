from src.toolkit.errors import unknown_conversion_units
from src.toolkit.errors import wrong_conversion_unit


length_cnostants={
    "meters": 1,
    "kilometers": 1000,
    "millimeters": 0.001,
    "centimetres": 0.01
}

mass_constants={
    "kilogram": 1000,
    "gram": 1,
    "milligram": 0.01,
    "ton": 1000000
}

def length_converter(inpt_length:float, inpt_units:str, output_units:str)->float:
    if inpt_units not in length_cnostants or output_units not in length_cnostants:
        return unknown_conversion_units()
    inpt_length*=length_cnostants[inpt_units]
    return inpt_length/length_cnostants[output_units]

def mass_converter(inpt_mass:float, inpt_units:str, output_units:str)->float:
    try:
        inpt_mass*=mass_constants[inpt_units]
    except:
        return wrong_conversion_unit()
    if inpt_units not in mass_constants or output_units not in mass_constants:
        return unknown_conversion_units()
    return inpt_mass/mass_constants[output_units]




