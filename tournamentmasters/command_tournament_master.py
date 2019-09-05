from bots import BaseBot
from tournamentmasters.tournament_master import TournamentMaster


class CommandTournamentMaster(TournamentMaster):

    def on_turn_end(self, bot_played: BaseBot):
        self.grid.print()
        print("---------------------\n")

    def on_winner_found(self, winner_bot: BaseBot):
        print(f'{winner_bot.name} {winner_bot.id} WOOOOOOON')
