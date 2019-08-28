from bots import BaseBot
from bots.botutilities import Grid


class TournamentMaster:

    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int):
        self.bot_1 = bot_1
        self.bot_2 = bot_2
        self.turn = 0
        self.grid = Grid.create(grid_width, grid_height)

    def current_turns_bot(self):
        """
        Selects which bot's turn it is. Can be overriden for different starting techniques or multiple turns in a row.
        :return: The bot which gets the next turn.
        """
        if self.turn % 2 == 0:
            return self.bot_1
        else:
            return self.bot_2

    def play_turn(self):
        bot = self.current_turns_bot()
        bot.update_grid(self.grid)
        decision = bot.get_guess()
        if self.validate_guess(decision):
            self.set_chip_at(decision, bot.id)

        self.turn += 1

    def validate_guess(self, guess: int) -> bool:
        return True

    def set_chip_at(self, column: int, bot_id: int):
        pass
