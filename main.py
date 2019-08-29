from bots.DummyBot import DummyBot
from CommandTournamentMaster import CommandTournamentMaster

if __name__ == '__main__':
    bot_1 = DummyBot(1)
    bot_2 = DummyBot(2)
    master = CommandTournamentMaster(bot_1, bot_2, 7, 7)
    master.play()
