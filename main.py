from CommandTournamentMaster import CommandTournamentMaster
from bots.DummyBot import DummyBot

if __name__ == '__main__':
    """app = QApplication([])
    painter = Painter()
    app.exec_()
"""
    bot_1 = DummyBot(1)
    bot_2 = DummyBot(3)
    master = CommandTournamentMaster(bot_1, bot_2, 7, 7)
    master.play()
