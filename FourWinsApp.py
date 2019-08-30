from PyQt5.QtWidgets import QApplication

from ThreadedTournamentMaster import ThreadedTournamentMaster
from bots import BaseBot
from interface import GridRenderer


class FourWinsApp(QApplication):

    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int):
        super().__init__([])

        self.tournament_thread = ThreadedTournamentMaster(bot_1, bot_2, grid_width, grid_height)
        self.tournament_thread.start()

        self.grid.set_at(2, 0, 1)
        self.grid.set_at(5, 1, 3)
        self.grid.set_at(0, 6, 1)
        app = QApplication([])
        self.renderer = GridRenderer(self)
        self.renderer.show()
        app.exec_()

    def on_turn_end(self, bot_played: BaseBot):
        self.renderer.update()

    def play(self):
        pass
