from typing import Optional, List, Type

from .basebot import BaseBot


def get_all_bots() -> List[Type[BaseBot]]:
    return BaseBot.__subclasses__()


def get_bot_with_name(name: str) -> Optional[Type[BaseBot]]:
    return next((x for x in get_all_bots() if x.name == name), None)


def get_all_bot_names():
    return [bot.name for bot in get_all_bots()]
