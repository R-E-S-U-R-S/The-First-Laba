def calc_error_unknown_input_simbol():
    print("Calc error: unknown input symbol")
    return "Calculation failed"


def wrong_conversion_unit():
    print("Wrong or unsupported conversion unit")
    return "Calculation failed"

def unknown_conversion_type():
    print("Unknown conversion type. Please enter: mass or length")
    return "Calculation failed"

def unknown_conversion_units():
    print("Unknown conversion unit. Supported units: mass: milligrams, grams, kilograms, tons; length: millimeters, centimeters, meters, kilometers")
    return "Calculation failed"