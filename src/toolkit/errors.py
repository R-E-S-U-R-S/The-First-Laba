import typer

class CalcErrors(Exception):
    # TODO норм док стрингу доделай
    """Calc error: unknown input symbol"""
    def __init__(self, error_message):
        super().__init__(f"Calc error: {typer.style(error_message, fg=typer.colors.RED, bold=True)}")


class ConvErrors(Exception):
    def __init__(self, error_message: str):
        super().__init__(f"Convertion error: {typer.style(error_message, fg=typer.colors.RED, bold=True)}")

if __name__ == "__main__":
    raise CalcErrors("Чёта не работает")