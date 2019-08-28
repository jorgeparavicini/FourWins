from bots.basebot import BaseBot, CellState

if __name__ == '__main__':
    bot = BaseBot(1, 5, 10)
    bot.current_grid[2][1] = CellState.mine
    bot.print_grid()
