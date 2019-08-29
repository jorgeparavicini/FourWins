from TournamentMaster import TournamentMaster


class CommandTournamentMaster(TournamentMaster):

    def play(self):
        while True:
            self.play_turn()
            self.grid.print()
