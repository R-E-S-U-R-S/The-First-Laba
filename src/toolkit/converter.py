from src.toolkit.errors import  ConvErrors

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

def length_converter(inpt_length:float, inpt_units:str, output_units:str):
    if inpt_units not in length_cnostants or output_units not in length_cnostants:
        raise ConvErrors("Unknown conversion unit")
    inpt_length*=length_cnostants[inpt_units]
    return inpt_length/length_cnostants[output_units]

def mass_converter(inpt_mass:float, inpt_units:str, output_units:str):
    try:
        inpt_mass*=mass_constants[inpt_units]
    except:
        raise ConvErrors("Unknown conversion unit")
    if inpt_units not in mass_constants or output_units not in mass_constants:
        raise ConvErrors("Unknown conversion unit")
    return inpt_mass/mass_constants[output_units]

def temp_converter(inpt_temp:float, inpt_units:str, output_units:str):
    if inpt_units.lower() == "celsius":
        if float(inpt_temp) <= -273.15:
            raise ConvErrors("Impossible low temperature")
    elif inpt_units.lower() == "fahrenheit":
        if float(inpt_temp) <= -459.67:
            raise ConvErrors("Impossible low temperature")
    elif inpt_units.lower() == "kelvin":
        if float(inpt_temp) <= 0:
            raise ConvErrors("Impossible low temperature")

    if inpt_units.lower()=="celsius" and output_units.lower()=="fahrenheit":
        return inpt_temp*1.8+32
    elif inpt_units.lower() == "celsius" and output_units.lower() == "kelvin":
        return inpt_temp + 273.15
    elif inpt_units.lower() == "fahrenheit" and output_units.lower() == "celsius":
        return (inpt_temp - 32) / 1.8
    elif inpt_units.lower() == "fahrenheit" and output_units.lower() == "kelvin":
        return (inpt_temp + 459.67) * (5/9)
    elif inpt_units.lower() == "kelvin" and output_units.lower() == "fahrenheit":
        return inpt_temp * 1.8 - 459.67
    elif inpt_units.lower() == "kelvin" and output_units.lower() == "celsius":
        return inpt_temp - 273.15
    elif inpt_units==output_units:
        return inpt_temp
    else:
        raise ConvErrors("Unknown conversion unit")