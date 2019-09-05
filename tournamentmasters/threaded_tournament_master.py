from PyQt5.QtCore import QThread

from bots import BaseBot
from tournamentmasters.tournament_master import TournamentMaster


class ThreadedTournamentMaster(QThread, TournamentMaster):
    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int):
        super(QThread, self).__init__(self)
        super(TournamentMaster, self).__init__(bot_1, bot_2, grid_width, grid_height)

    def __del__(self):
        # self.wait()
        pass

    def run(self) -> None:
        while True:
            pass

    def play(self):
        pass
