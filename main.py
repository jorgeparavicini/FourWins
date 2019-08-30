from FourWinsApp import FourWinsApp
from bots.DummyBot import DummyBot

if __name__ == '__main__':

    bot_1 = DummyBot(1)
    bot_2 = DummyBot(3)
    master = FourWinsApp(bot_1, bot_2, 7, 7)
    # master = CommandTournamentMaster(bot_1, bot_2, 7, 7)
    master.play()
