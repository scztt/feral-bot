from typing import Optional, List
import random
import typer
from typer.testing import CliRunner


# COMMAND LINE TOOLS
app = typer.Typer()


def run_from_message(message:str):
    runner = CliRunner()
    return runner.invoke(app, message).output


#######################################################################################
# COMMANDS
@app.command()
def greet(name: str):
    print(f"Hello there {name}")

@app.command()
def shuffle(items: List[str]):
    random.shuffle(items)
    print(", ".join(items))

#
#######################################################################################


if __name__ == "__main__":
    app()
