import random
from time import time
from html import escape

from mautrix.types import (
    TextMessageEventContent,
    MessageType,
    Format,
    RelatesTo,
    RelationType,
)
from maubot import Plugin, MessageEvent
from maubot.handlers import command

from commands import run_from_message, app, CommandInfo


def needs_monospace(text: str) -> bool:
    """
    Check if the text contains any characters that require monospace formatting.
    This includes characters like `, `, and `\n`.
    """
    finds = [
        "    ",  # four spaces
        "\t",  # tab
        "─────",  # long dash
    ]
    for find in finds:
        if text.find(find) != -1:
            return True

    return False


def make_command(cls, function, name, decorators):
    async def invoke_command(self, event: MessageEvent, match):
        message = event.content.body
        message = message[1:] if message.startswith("!") else message
        result = run_from_message(f"{message}")
        self.log.debug(
            f"ran cmd line: {message} (needs_monospace = {needs_monospace(result)})"
        )
        if needs_monospace(result):
            result = f"""
```
{result}
```
            """
            await event.respond(result, markdown=True)
        else:
            await event.respond(result, markdown=False, allow_html=True)

    for decorator in decorators:
        invoke_command = decorator(invoke_command)

    setattr(cls, name, invoke_command)


def make_command_from_info(cls, info: CommandInfo):
    name = info.name or info.callback.__name__
    function = info.callback
    print(f"trying to register command: {name}")
    decorators = [command.passive(name, multiple=True)]

    make_command(cls, function, name, decorators)


class FeralBot(Plugin):
    pass


for registered in app.registered_commands:
    make_command_from_info(FeralBot, registered)
