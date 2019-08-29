import random

from bots.basebot import BaseBot, CellState


class DummyBot(BaseBot) :
    def get_guess(self) -> int:
        while True:
            choice = random.randint(0, 2)
            if self.grid.at(choice, self.grid.height - 1) == CellState.empty:
                print(f"Bot {self.id}'s choice is: {choice}")
                return choice
