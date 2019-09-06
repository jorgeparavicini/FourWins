import random

from . import BaseBot, CellState


class DummyBot(BaseBot):
    name = "Dummy Bot"

    def get_guess(self) -> int:
        while True:
            choice = random.randint(0, self.grid.width - 1)
            if self.grid.at(choice, self.grid.height - 1) == CellState.empty:
                print(f"Bot {self.id}'s choice is: {choice}")
                return choice
