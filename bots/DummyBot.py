from bots.basebot import BaseBot, CellState
import random

class DummyBot(BaseBot) :
    def get_guess(self) -> int:
        while True:
            choice = random.randint(0, 6)
            if self.grid.at(0, choice) == CellState.empty:
                print(f"Bot {self.id}'s choice is: {choice}")
                return choice
