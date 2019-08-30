from bots import BaseBot
from bots.botutilities import Grid


class TournamentMaster:
    win_condition = 4

    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int):
        self.bot_1 = bot_1
        self.bot_2 = bot_2
        self.turn = 0
        self.grid = Grid.create(grid_width, grid_height)

    def current_turns_bot(self):
        """
        Selects which bot's turn it is. Can be overridden for different starting techniques or multiple turns in a row.
        :return: The bot which gets the next turn.
        """
        if self.turn % 2 == 0:
            return self.bot_1
        else:
            return self.bot_2

    def play_turn(self) -> (int, int):
        bot = self.current_turns_bot()
        bot.update_grid(self.grid)
        # Implement safe switch so they cant enter infinite loop
        decision = bot.get_guess()
        if self.validate_guess(decision):
            row = self.get_row_for_first_empty_cell_in_column(decision)
            self.set_chip(bot.id, decision, row)
        else:
            print("INVALID GUESS")
            return None

        self.turn += 1
        return decision, row

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

    def check_if_bot_won_at(self, bot_id: int, x: int, y: int) -> bool:
        """
        Checks if there is a winner on the current grid.
        :returns 0 If there are no winners, otherwise the winners bot's id is
        """
        assert (0 <= x < self.grid.width)
        assert (0 <= y < self.grid.height)

        horizontal = self.grid.check_horizontal_group_at(bot_id, x, y)
        vertical = self.grid.check_vertical_group_at(bot_id, x, y)
        diagonal_forward = self.grid.check_forward_diagonal_group_at(bot_id, x, y)
        diagonal_backward = self.grid.check_backward_diagonal_group_at(bot_id, x, y)
        """print(f'Horizontal: {horizontal} \n'
              f'Vertical:   {vertical} \n'
              f'Dia Back:   {diagonal_backward} \n'
              f'Dia For:    {diagonal_forward} \n')
"""
        max_group = max(horizontal, vertical, diagonal_forward, diagonal_backward)
        if max_group >= self.win_condition:
            return True
        return False

    def play(self):
        while True:
            current_bot = self.current_turns_bot()
            placed_location = self.play_turn()

            self.on_turn_end(current_bot)

            # Check for winner
            if placed_location is None:
                continue
            if self.check_if_bot_won_at(current_bot.id, placed_location[0], placed_location[1]):
                self.on_winner_found(current_bot)
                break

    def on_turn_end(self, bot_played: BaseBot):
        pass

    def on_winner_found(self, winner_bot: BaseBot):
        pass
