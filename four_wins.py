import argparse
import sys

from bots import bot_manager
from interface.mainwindow import MainWindow
from tournamentmasters.command_tournament_master import CommandTournamentMaster


def get_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Play a game of four wins with 2 Bots.")
    p.add_argument("-b1", "--bot_1", help="The name of the first bot", type=str, required="-p" not in sys.argv)
    p.add_argument("-b2", "--bot_2", help="The name of the second bot", type=str, required="-p" not in sys.argv)
    p.add_argument("-p", "--print_bots", help="Print the names of all available Bots", action="store_true",
                   required=False)
    p.add_argument("-g", "--gui", help="Render the game to a window", action="store_true", required=False)
    p.add_argument("-W", "--width", help="The width of the game grid", type=int, default=7, required=False)
    p.add_argument("-H", "--height", help="The height of the game grid", type=int, default=7, required=False)

    p.add_argument("-t", "--time", help="The time in seconds(float) after each round has been played", type=float,
                   default=0.0, required=False)
    return p.parse_args()


if __name__ == '__main__':

    parser = get_args()
    if parser.print_bots:
        print(bot_manager.get_all_bot_names())
        exit(0)

    bot_1 = bot_manager.get_bot_with_name(parser.bot_1)
    if bot_1 is None:
        print(f"Failed to get bot with name: {parser.bot_1} no bot with that name.")
        exit(-1)

    bot_2 = bot_manager.get_bot_with_name(parser.bot_2)
    if bot_2 is None:
        print(f"Failed to get bot with name: {parser.bot_2} no bot with that name.")
        exit(-1)

    if parser.gui:
        MainWindow(bot_1(1), bot_2(2), parser.width, parser.height, parser.time)
    else:
        tournament = CommandTournamentMaster(bot_1(1), bot_2(2), parser.width, parser.height, parser.time)
        tournament.play()
