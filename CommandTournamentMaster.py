from TournamentMaster import TournamentMaster
from bots import BaseBot


class CommandTournamentMaster(TournamentMaster):

    def on_turn_end(self, bot_played: BaseBot):
        self.grid.print()

    def on_winner_found(self, winner_bot: BaseBot):
        print(f'Bot {winner_bot.id} WOOOOOOON')
