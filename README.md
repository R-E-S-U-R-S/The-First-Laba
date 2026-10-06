# The First Laba

A small Python command-line toolkit that provides:

- an arithmetic expression calculator;
- a unit converter for length, mass, and temperature;
- a simple test suite;
- a Makefile command for running tests.

The project is implemented in Python and uses [Typer](https://typer.tiangolo.com/) to expose its command-line interface.

## Features

### Calculator

The calculator evaluates arithmetic expressions containing:

- addition: `+`
- subtraction: `-`
- multiplication: `*`
- division: `/`
- floor division: `//`
- modulo: `%`
- exponentiation: `**`
- parentheses
- positive and negative numbers
- configurable result rounding

The calculator processes operations according to the order implemented in the expression evaluator and returns either an integer or a rounded floating-point value.

### Unit converter

The converter supports three categories:

- **Length**
- **Mass**
- **Temperature**

Supported length units:

| Unit | Name |
|---|---|
| `meters` | meters |
| `kilometers` | kilometers |
| `millimeters` | millimeters |
| `centimetres` | centimetres |

Supported mass units:

| Unit | Name |
|---|---|
| `kilogram` | kilogram |
| `gram` | gram |
| `milligram` | milligram |
| `ton` | metric ton |

Supported temperature units:

- `celsius`
- `fahrenheit`
- `kelvin`

The converter validates units and rejects physically impossible temperatures below the corresponding absolute minimum.

## Project Structure

```text
The-First-Laba/
├── src/
│   └── toolkit/
│       ├── calculator.py
│       ├── constants.py
│       ├── converter.py
│       └── errors.py
├── test/
├── .idea/
├── __init__.py
├── __main__.py
├── Makefile
└── pyproject.toml
```

### Main components

#### `__main__.py`

The CLI entry point.

It creates a Typer application and exposes two commands:

```text
calculation
convert
```

The application imports the calculator and conversion functions from `src/toolkit`.

#### `src/toolkit/calculator.py`

Contains the arithmetic expression evaluator.

The implementation first tokenizes an input expression into numbers and operators, evaluates expressions inside parentheses, and then applies the supported operations.

Supported operators are:

```text
**
*
/
//
//
+
-
%
```

More precisely, the implementation recognizes:

```text
**
*
/
//
%
+
-
```

#### `src/toolkit/converter.py`

Contains the three conversion functions:

```python
length_converter(...)
mass_converter(...)
temp_converter(...)
```

Length and mass conversions are based on constants defined in `constants.py`. Temperature conversions use explicit Celsius/Fahrenheit/Kelvin formulas.

#### `src/toolkit/constants.py`

Stores conversion factors and minimum valid temperatures.

#### `src/toolkit/errors.py`

Defines custom exceptions:

```python
CalcErrors
ConvErrors
```

These exceptions are used to report invalid calculator expressions and conversion errors.

---

## Requirements

The project's `pyproject.toml` currently specifies:

```text
Python >= 3.14
```

and does not declare runtime dependencies.

However, the CLI imports `typer`, so Typer must be installed before running the application.

### Recommended environment

Create a virtual environment:

```bash
python3.14 -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the missing CLI dependency:

```bash
python -m pip install typer
```

It is recommended to upgrade `pip` first:

```bash
python -m pip install --upgrade pip
python -m pip install typer
```

---

## First Run

Clone the repository:

```bash
git clone https://github.com/R-E-S-U-R-S/The-First-Laba.git
cd The-First-Laba
```

Create and activate a virtual environment:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

Install Typer:

```bash
python -m pip install typer
```

The application can then be started directly through `__main__.py`:

```bash
python __main__.py --help
```

You should see the available commands, including:

```text
calculation
convert
```

---

# Usage

## Calculator

The calculator is invoked with:

```bash
python __main__.py calculation "<expression>"
```

For example:

```bash
python __main__.py calculation "2+2"
```

Result:

```text
Calculation answer: 4
```

### Multiplication

```bash
python __main__.py calculation "6*7"
```

### Division

```bash
python __main__.py calculation "20/4"
```

### Floor division

```bash
python __main__.py calculation "20//3"
```

### Modulo

```bash
python __main__.py calculation "20%3"
```

### Exponentiation

```bash
python __main__.py calculation "2**8"
```

### Parentheses

```bash
python __main__.py calculation "(2+3)*4"
```

### Negative numbers

If an expression begins with `-`, pass `--` before the expression so that the command-line parser does not interpret the leading dash as an option:

```bash
python __main__.py calculation -- "-2+5"
```

### Rounding

The calculator accepts an optional `digit_round` argument.

The default is:

```text
5
```

To specify another number of decimal places:

```bash
python __main__.py calculation "10/3" --digit-round 2
```

Depending on the installed Typer version, the option may also be exposed using its underscore form:

```bash
python __main__.py calculation "10/3" --digit_round 2
```

The value is passed directly to Python's `round()` function for non-integer results.

---

# Unit Converter

The converter is invoked with:

```bash
python __main__.py convert <type>
```

The available converter types are:

```text
length
mass
temperature
```

After starting the command, the application interactively asks for:

```text
Input number, input unit, output unit:
```

Enter the three values separated by spaces.

---

## Length Conversion

Start the length converter:

```bash
python __main__.py convert length
```

Then enter, for example:

```text
1000 meters kilometers
```

The program prints:

```text
Conversion result: 1.0 kilometers
```

Supported units:

```text
meters
kilometers
millimeters
centimetres
```

Examples:

```text
1 kilometers meters
```

```text
100 centimetres meters
```

```text
5000 millimeters meters
```

Length values must be positive.

---

## Mass Conversion

Start the mass converter:

```bash
python __main__.py convert mass
```

For example:

```text
1000 gram kilogram
```

The result is:

```text
Conversion result: 1.0 kilogram
```

Supported units:

```text
kilogram
gram
milligram
ton
```

Examples:

```text
5 kilogram gram
```

```text
2500 gram kilogram
```

```text
2 ton kilogram
```

Mass values must be positive.

---

## Temperature Conversion

Start the temperature converter:

```bash
python __main__.py convert temperature
```

For example:

```text
100 celsius fahrenheit
```

The result is:

```text
Conversion result: 212.0 fahrenheit
```

Supported temperature units:

```text
celsius
fahrenheit
kelvin
```

Examples:

```text
0 celsius fahrenheit
```

```text
100 celsius kelvin
```

```text
32 fahrenheit celsius
```

```text
273.15 kelvin celsius
```

```text
300 kelvin fahrenheit
```

The implementation prevents temperatures below the physical lower bound for the selected scale:

```text
Celsius:    -273.15
Fahrenheit: -459.67
Kelvin:        0
```

These limits are defined in `constants.py`.

---

# Error Handling

The project defines two custom exception types:

```python
CalcErrors
ConvErrors
```

Calculator errors are used for invalid expressions and invalid operations such as division by zero.

For example, an invalid calculator expression can produce an error similar to:

```text
Calc error: Unknown input symbol
```

Division by zero is explicitly checked by the calculator:

```text
Calc error: Zero division
```

Conversion errors include invalid units:

```text
Convertion error: Unknown conversion unit
```

The spelling `Convertion` is part of the current exception implementation.

---

# Running Tests

The repository includes a `test` directory and provides a Makefile target for running the test suite.

Run all tests with:

```bash
make tests
```

The Makefile expands this command to:

```bash
python -m pytest -v
```

Therefore, if `make` is unavailable, the equivalent command is:

```bash
python -m pytest -v
```

The Makefile currently contains only the `tests` target.

If pytest is not installed in the environment:

```bash
python -m pip install pytest
```

Then:

```bash
make tests
```

---

# Running Without Make

You do not need Make to use the application.

Run the CLI directly:

```bash
python __main__.py --help
```

Calculator:

```bash
python __main__.py calculation "2+2"
```

Length converter:

```bash
python __main__.py convert length
```

Mass converter:

```bash
python __main__.py convert mass
```

Temperature converter:

```bash
python __main__.py convert temperature
```

Tests:

```bash
python -m pytest -v
```

---

# Command Reference

| Command | Description |
|---|---|
| `python __main__.py --help` | Show CLI help |
| `python __main__.py calculation "<expression>"` | Evaluate an arithmetic expression |
| `python __main__.py calculation "<expression>" --digit-round N` | Evaluate and round the result to `N` digits |
| `python __main__.py convert length` | Start the length converter |
| `python __main__.py convert mass` | Start the mass converter |
| `python __main__.py convert temperature` | Start the temperature converter |
| `make tests` | Run the test suite with pytest |
| `python -m pytest -v` | Run the test suite without Make |

---

# Architecture Overview

The application has a simple layered structure:

```text
                 ┌─────────────────┐
                 │   __main__.py   │
                 │    Typer CLI    │
                 └────────┬────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
    ┌─────────────────┐      ┌─────────────────┐
    │   calculator.py │      │   converter.py  │
    │                 │      │                 │
    │ Expression      │      │ Length          │
    │ evaluation      │      │ Mass            │
    │                 │      │ Temperature     │
    └────────┬────────┘      └────────┬────────┘
             │                        │
             ▼                        ▼
    ┌─────────────────┐      ┌─────────────────┐
    │    errors.py    │      │  constants.py   │
    │                 │      │                 │
    │ CalcErrors      │      │ Conversion      │
    │ ConvErrors      │      │ factors / limits│
    └─────────────────┘      └─────────────────┘
```

The CLI is intentionally thin: it collects command-line or interactive input and delegates the actual work to the toolkit modules.

---

# Development Notes

## Package Metadata

The project is currently described in `pyproject.toml` as:

```toml
[project]
name = "the-first-laba-conerter-dev"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = []
```

Note that the project name contains the existing spelling `conerter`; this README preserves the repository's current metadata rather than silently changing it.

## Dependency Declaration

Although `dependencies = []` is currently specified, the source imports Typer:

```python
import typer
```

Therefore, a fresh environment needs Typer installed manually before the CLI can be executed.

For reproducible installation, the project's packaging configuration should eventually declare Typer as a dependency.

For example:

```toml
[project]
name = "the-first-laba-conerter-dev"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "typer",
]
```

This change is not required if dependencies continue to be managed manually, but it would make the project easier to install and distribute.

---

# Known Implementation Details

A few behaviors are worth knowing when using or extending the project.

### Calculator input

The calculator uses its own tokenizer and evaluator rather than Python's `eval()`. Expressions are parsed into numbers and operations before being evaluated.

### Parentheses

Parenthesized expressions are evaluated recursively before the remaining expression is processed.

### Rounding

The calculator returns an integer when the final result has no fractional part. Otherwise, the result is rounded using the requested number of digits.

### Interactive conversion input

The converter expects the input to be entered as three space-separated values:

```text
<number> <input unit> <output unit>
```

For example:

```text
1000 meters kilometers
```

### Conversion constants

Length and mass conversions use a common base-unit representation defined in `constants.py`.

---

# Quick Start

For the shortest possible setup:

```bash
git clone https://github.com/R-E-S-U-R-S/The-First-Laba.git
cd The-First-Laba

python3.14 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install typer pytest

python __main__.py --help
```

Try the calculator:

```bash
python __main__.py calculation "2**8"
```

Try a converter:

```bash
python __main__.py convert length
```

Then enter:

```text
1000 meters kilometers
```

Run the tests:

```bash
make tests
```

or:

```bash
python -m pytest -v
```

---

# License

No license file is currently listed in the repository. If this project is intended to be publicly reusable, consider adding an explicit open-source license.
