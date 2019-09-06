from bots import BaseBot
from tournamentmasters.tournament_master import TournamentMaster


class CommandTournamentMaster(TournamentMaster):

    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int,
                 time_between_rounds: float = 0):
        super(CommandTournamentMaster, self).__init__(bot_1, bot_2, grid_width, grid_height, time_between_rounds)
        self.winner_id = -1

    def on_turn_end(self, bot_played: BaseBot):
        self.grid.print()
        print("---------------------\n")

    def on_winner_found(self, winner_bot: BaseBot):
        print(f'{winner_bot.name} {winner_bot.id} WOOOOOOON')
        self.winner_id = winner_bot.id

    def play(self):
        super().play()
        return self.winner_id
