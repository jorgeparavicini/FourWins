from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

from bots import BaseBot
from tournamentmasters.tournament_master import TournamentMaster


class TournamentThread(QThread):
    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, grid_width: int, grid_height: int, time: float):
        super().__init__()

        self.__is_done = False
        self.__did_initialize = False

        self.tournament_master = TournamentMaster(bot_1, bot_2, grid_width, grid_height, time)
        self.tournament_master.on_winner_found_cb.append(self.on_winner_found)
        self.tournament_master.on_turn_end_cb.append(self.on_turn_end)

    @property
    def is_done(self):
        return self.__is_done

    def __del__(self):
        self.wait()

    def toggle_pause(self):
        if not self.__did_initialize:
            self.start()
            self.__did_initialize = True
            self.did_start.emit()
        else:
            self.tournament_master.is_paused = not self.tournament_master.is_paused
            self.did_toggle_pause.emit()

    def stop(self):
        self.tournament_master.did_stop = True
        self.did_stop.emit()

    def on_winner_found(self, bot: BaseBot):
        self.__is_done = True
        self.winner_found.emit(bot)

    def on_turn_end(self, bot: BaseBot):
        self.turn_ended.emit(bot)

    winner_found = pyqtSignal(BaseBot)
    turn_ended = pyqtSignal(BaseBot)
    did_start = pyqtSignal()
    did_toggle_pause = pyqtSignal()
    did_stop = pyqtSignal()

    def run(self) -> None:
        self.tournament_master.play()
