from CommandTournamentMaster import CommandTournamentMaster
from bots.DummyBot import DummyBot

if __name__ == '__main__':

    bot_1 = DummyBot(1)
    bot_2 = DummyBot(2)
    master = CommandTournamentMaster(bot_1, bot_2, 3, 3)
    master.play()
