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
        # Implement safe switch so they cant enter infinite loop
        decision = bot.get_guess()
        if self.validate_guess(decision):
            row = self.get_row_for_first_empty_cell_in_column(decision)
            self.set_chip(bot.id, decision, row)
        else:
            print("INVALID GUESS")

        self.turn += 1

    def validate_guess(self, guess: int) -> bool:
        return not self.grid.is_column_full(guess)

    def get_row_for_first_empty_cell_in_column(self, column: int):
        return self.get_highest_chip_for_column(column)

    def set_chip(self, bot_id: int, column: int, row: int):
        self.grid.set_at(column, row, bot_id)

    def get_highest_chip_for_column(self, column: int) -> int:
        for i, value in enumerate(self.grid.column(column)):
            if value is 0:
                return min(i, self.grid.height)
        return self.grid.height
