from abc import ABC, abstractmethod
from enum import Enum

from .botutilities import Grid

"""
This is the base class for all Bots Participating in the Fight of the CENTURY

Each function explains what it does more or less in detail. If you haven't done so already here is a quick summary
on how you create your own Bot. For further reading, head to the README.md file

Without further ado lets get into the fun.
We all know the game FourWins.
There is a game space - We call it *GRID*- which has a width X and a height Y.
The game plays out in turns, so your bot will face against another bot, theoretically you can also compete against
yourself but where is the fun in that.
Each turn the bot which has its turn, can tell the Tournament manager - The controller of the game - 
where he wants to place its *CHIP* the Tournament validates that decision and updates the playing field 
for both bots.

This keeps going on 1 by 1 until one bot gets 4 of his Chips in a row either vertically, horizontally or diagonally.
"""


class CellState(Enum):
    """
    This class represents the state of one position in a game grid.
    If you call the 'get_state_at' function on your Bot you will get one of these values as your return type.
    Each of the following states will be explained shortly, just keep in mind, that
    ** Each state is for -one- specific Cell in the game **
    - Empty:
        The Empty state means, that in this cell there is no chip of either player. Obviously this means that there
        is none located above it either. (If it would please report a bug :))
    - Mine:
        This gets analyzed with the id of your bot, and is you get this state if there is a chip on the requested
        position and that chip was placed by your bot.
    - Enemy:
        Logically the last state means that there is also a chip but it isn't yours, therefore it is the
        enemies bot's chip.
    """
    empty = 0
    mine = 1
    enemy = 2


class BaseBot(ABC):

    # Change this variable in your bot class, to give your bot a cool name.
    name = "Base Bot"

    def __init__(self, bot_id: int, grid: Grid[int]):
        """
        Create a new Bot from an id, and a grid created by the Tournament Manager.
        :param bot_id: The id of this bot - see the id property for further details
        :param grid: The grid of this game - see the grid property for further details
        """
        self.__id = bot_id
        self.__grid = grid.map(self.__cell_state_from_id)

    @property
    def id(self):
        """
        Every bot needs to be identifiable by the Tournament Manager for multiple reasons.
        You can ignore this value.
        :return: The id of this bot.
        """
        return self.__id

    @property
    def grid(self):
        """
        This is the Games representation of the playing field.
        It consists of 2 axis X and Y. Both default to 7 but it is not guaranteed to be.
        So make sure your bot supports a generic size if you want to challenge yourself even further.

        Basically this is just a 2D List, where each element with position x, and y has a current CellState.
        Read the documentation for the CellState to understand what each possible state represents.

        :return: A read only representation of the Game Field.
        """
        return self.__grid

    # This method will be called from the Tournament Manager.
    # IMPORTANT - DO NOT OVERRIDE THIS METHOD
    def update_grid(self, new_grid: Grid[int]):
        """
        Updates the internal variable of the grid.
        Before setting it, it will map (convert) all integer values from the Grid to a CellState that makes sense
        to this bot. For example, if this bot's id is 2 and a field has a value of 2, that value will be converted
        to CellState.mine. If it is 0 it will be converted to CellState.empty and everything else can be assumed
        is a chip of the enemy player.
        :param new_grid: The new grid in integer representation, as given by the Tournament Manager.
        """
        # Map the new list to Cell States
        self.__grid = new_grid.map(self.__cell_state_from_id)

    @abstractmethod
    def get_guess(self) -> int:
        """
        This method will be called when it is your turn to add a chip.
        You can be certain that the grid has already been updated by the Tournament Manager
        when this method gets called.
        An integer value is expected to be returned that represents the column in which you want to place your chip.
        IMPORTANT:
        - The columns start from 0-(n-1) where n would be the game width.
        - If your response is outside of the above said range, your decision will be taken  as invalid and
        your opponent can continue with your turn being wasted.
        """
        pass

    def get_state_at(self, x: int, y: int) -> CellState:
        """
        Most information about the game state should be taken directly from the 'grid'.
        This is just a helper method that bridges the 'at' function of the grid for easier access.

        It gets the Cell State of the passed index.
        :param x: The x position of which you want to check the state for.
        :param y: The y position of which you want to check the state for.
        :return: The State of the passed index.
        """
        return self.grid.at(x, y)

    def __cell_state_from_id(self, n: int) -> CellState:
        """
        This is an internal function that converts an integer passed from the Tournament Managers grid
        to a CellState.
        You can call this, but it should never make any sense, as the grid has already been translated.
        :param n: The integer to convert.
        :return: The corresponding state for the passed integer.
        """
        if n == 0:
            return CellState.empty
        elif n == self.id:
            return CellState.mine
        else:
            return CellState.enemy
