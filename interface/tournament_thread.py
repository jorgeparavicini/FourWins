from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

from bots import BaseBot
from tournamentmasters.tournament_master import TournamentMaster


class TournamentThread(QThread):
    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int, time: float):
        super().__init__()

        self.tournament_master = TournamentMaster(bot_1, bot_2, grid_width, grid_height, time)
        self.tournament_master.on_winner_found_cb.append(self.on_winner_found)
        self.tournament_master.on_turn_end_cb.append(self.on_turn_end)

    def __del__(self):
        self.wait()

    def play(self):
        pass

    def on_winner_found(self, bot: BaseBot):
        self.winner_found.emit(bot)

    def on_turn_end(self, bot: BaseBot):
        self.turn_ended.emit(bot)

    winner_found = pyqtSignal(BaseBot)
    turn_ended = pyqtSignal(BaseBot)

    def run(self) -> None:
        self.tournament_master.play()
