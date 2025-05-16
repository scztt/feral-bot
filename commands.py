from typing import Annotated, Optional, List
import random
import typer
from typer.testing import CliRunner
from typer.models import CommandInfo

from poems import poems

# COMMAND LINE TOOLS
app = typer.Typer()


@app.callback()
def callback():
    pass


def run_from_message(message: str):
    runner = CliRunner()
    return runner.invoke(app, message).output


#######################################################################################
# COMMANDS
@app.command()
def poem():
    poem = random.choice(poems)
    print(poem)


#
#######################################################################################


if __name__ == "__main__":
    app()
