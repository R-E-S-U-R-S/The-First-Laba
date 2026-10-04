import typer
import sys

from src.toolkit.calculator import calc
from src.toolkit.converter import length_converter, mass_converter, temp_converter

app = typer.Typer()

@app.command()
def convert(convert_units_type:str):
    """Allows to convert length, temperature and mass units. Type mass/length/temperature to use mass or length converter. Requires additional input in next command in 'number, input units, output units' format. Please divide arguments using only space."""
    if convert_units_type != "length" and convert_units_type !="mass" and convert_units_type !="temperature":
        error_msg=typer.style("Unexpected convertion type. Please enter mass or length or temperature", fg=typer.colors.RED, bold=True)
        typer.echo(error_msg, err=True)
        sys.exit(2)

    inpt_str = input("Input number, input unit, output unit: ").split(" ")
    if convert_units_type.lower() == "temperature":
        pass

    elif float(inpt_str[0])<=0:
        error_msg = typer.style("Impossible length or mass. Please enter positive number", fg=typer.colors.RED, bold=True)
        typer.echo(error_msg, err=True)
        sys.exit(2)

    if convert_units_type.lower() == "mass":
        try:
            print(f"Conversion result: {mass_converter(float(inpt_str[0]), inpt_str[1], inpt_str[2])} {inpt_str[2]}")
        except Exception as e:
            typer.echo(str(e), fg=typer.colors.RED, err=True, bold=True)
            sys.exit(2)

    elif convert_units_type.lower() == 'length':
        try:
            print(f"Conversion result: {length_converter(float(inpt_str[0]), inpt_str[1], inpt_str[2])} {inpt_str[2]}")
        except Exception as e:
            typer.echo(str(e), fg=typer.colors.RED, err=True, bold=True)
            sys.exit(2)

    elif convert_units_type.lower() == 'temperature':
        try:
            print(f"Conversion result: {temp_converter(float(inpt_str[0]), inpt_str[1], inpt_str[2])} {inpt_str[2]}")
        except Exception as e:
            typer.echo(str(e), err=True)
            sys.exit(2)

@app.command()
def calculation(input_str:str):
    # todo -- перед отриц числами, если многа пробелов, то в кавычках
    """Runs simple calculation engine. Please type calculation sequence in brackets. If - is first letter, please put -- before sequence"""
    try:
        print(f"Calculation answer: {calc(input_str)}")
    except Exception as e:
        typer.echo(str(e))
        sys.exit(2)

if __name__ == "__main__":
    app()