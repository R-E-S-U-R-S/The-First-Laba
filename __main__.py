import typer
from src.toolkit.calculator import calc
from src.toolkit.converter import mass_converter
from src.toolkit.converter import length_converter
from src.toolkit.errors import unknown_conversion_type


app = typer.Typer()

@app.command()
def convert(convert_units_type:str):
    """Allows to convert length and mass units. Type mass/length to use mass or length converter. Requires additional input in next command in 'number, input units, output units' format. Please divide arguments using only space."""
    inpt_str = input("Input number, input unit, output unit: ").split(" ")
    try:
        if inpt_str[0]<=0:
            print("Impossible mass or length")
            return
    except:
        print("Calculation error try again")

    if convert_units_type.lower() == "mass":
         print(f"Conversion result: {mass_converter(float(inpt_str[0]), inpt_str[1], inpt_str[2])} {inpt_str[2]}")
    elif convert_units_type.lower() == 'length':
        print(f"Conversion result: {length_converter(float(inpt_str[0]), inpt_str[1], inpt_str[2])} {inpt_str[2]}")
    else:
        print(unknown_conversion_type())


@app.command()
def calculation(input_str:str):
    """Runs simple calculation engine. Please type calculation sequence in brackets."""
    print(f"Calculation answer: {calc(input_str)}")


if __name__ == "__main__":
    app()