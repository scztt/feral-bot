import random 
from time import time
from html import escape

from mautrix.types import TextMessageEventContent, MessageType, Format, RelatesTo, RelationType
from maubot import Plugin, MessageEvent
from maubot.handlers import command

from commands import run_from_message

class FeralBot(Plugin):
    @command.new("ping", help="Ping")
    @command.argument("message", pass_raw=True, required=False)
    async def ping_handler(self, evt: MessageEvent, message: str = "") -> None:
        await evt.respond("pong!")

    @command.new("greet", help="Greet a person")
    @command.argument("name", pass_raw=True)
    async def greet_handler(self, evt: MessageEvent, name: str) -> None:
        result = run_from_message("greet " + name)
        await evt.respond(result)

    @command.new("shuffle", help="Shuffle a list of items")
    @command.argument("items", pass_raw=True)
    async def shuffle_handler(self, evt: MessageEvent, items: str) -> None:
        result = run_from_message("shuffle " + items)
        await evt.respond(result)

