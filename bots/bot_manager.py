import importlib
import pkgutil
from pathlib import Path
from typing import Optional, List, Type

from .basebot import BaseBot

__imported = False


def import_all_bots():
    global __imported
    if __imported:
        return
    for (_, name, _) in pkgutil.iter_modules([Path(__file__).parent]):
        importlib.import_module('.' + name, package="bots")

    __imported = True


def get_all_bots() -> List[Type[BaseBot]]:
    import_all_bots()
    return BaseBot.__subclasses__()


def get_bot_with_name(name: str) -> Optional[Type[BaseBot]]:
    return next((x for x in get_all_bots() if x.name == name), None)


def get_all_bot_names():
    return [bot.name for bot in get_all_bots()]
