
class CalcErrors(Exception):
    # TODO норм док стрингу доделай
    """Calc error: unknown input symbol"""
    def __init__(self, error_message):
        super().__init__(f"Calc error: {error_message}")


class ConvErrors(Exception):
    # TODO норм ошибки сделай, да
    """Convertion error: unknown input symbol"""
    def __init__(self, error_message):
        super().__init__(f"Calc error: {error_message}")


def wrong_conversion_unit():
    print("Wrong or unsupported conversion unit")
    return "Calculation failed"

def unknown_conversion_type():
    print("Unknown conversion type. Please enter: mass or length")
    return "Calculation failed"

def unknown_conversion_units():
    print("Unknown conversion unit. Supported units: mass: milligrams, grams, kilograms, tons; length: millimeters, centimeters, meters, kilometers")
    return "Calculation failed"

if __name__ == "__main__":
    raise CalcErrors("Чёта не работает")