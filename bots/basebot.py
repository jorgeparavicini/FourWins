from typing import List
import abc
from enum import Enum


class CellState(Enum):
    empty = 0
    mine = 1
    enemy = 2


class BaseBot:
    __metaclass__ = abc.ABCMeta

    def __init__(self, bot_id: int, grid_width: int = 7, grid_height: int = 7):
        self.__id = bot_id
        self.__grid_width = grid_width
        self.__grid_height = grid_height
        self.__current_grid = [x[:] for x in [[CellState.empty] * grid_width] * grid_height]

    @property
    def id(self):
        return self.__id

    @property
    def grid_width(self):
        return self.__grid_width

    @property
    def grid_height(self):
        return self.__grid_height

    @property
    def current_grid(self):
        return self.__current_grid

    def update_grid(self, current_grid: List[List[int]]):
        # Map the new list to Cell States
        self.__current_grid = [list(map(self.__cell_state_from_id, row)) for row in current_grid]

    @abc.abstractmethod
    def get_guess(self) -> int:
        pass

    def get_id(self, x: int, y: int) -> CellState:
        return self.__current_grid[y][x]

    def __cell_state_from_id(self, n: int) -> CellState:
        if n == 0:
            return CellState.empty
        elif n == self.id:
            return CellState.mine
        else:
            return CellState.enemy

    def print_grid(self):
        for row in self.__current_grid:
            print(row)
