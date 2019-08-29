from TournamentMaster import TournamentMaster


class CommandTournamentMaster(TournamentMaster):

    def play(self):
        while True:
            current_bot = self.current_turns_bot()
            placed_location = self.play_turn()
            self.grid.print()
            if placed_location is None:
                continue
            if self.check_if_bot_won_at(current_bot.id, placed_location[0], placed_location[1]):
                print(f'Bot {current_bot.id} WOOOOOOON')
                break
