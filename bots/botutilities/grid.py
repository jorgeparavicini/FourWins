from __future__ import annotations
from typing import TypeVar, List, Generic, Callable
import warnings

T = TypeVar('T')


class Grid(Generic[T]):
    def __init__(self, grid: List[List[T]]):
        self.__grid = grid
        if len(grid) > 0 and len(grid[0]) > 0:
            self.__width = len(grid[0])
            self.__height = len(grid)
        else:
            warnings.warn("Grid has invalid size.")
            
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @classmethod
    def create(cls, width: int, height: int, default: T = 0) -> Grid[T]:
        return cls([x[:] for x in [[default] * width] * height])

    def at(self, x: int, y: int) -> T:
        return self.__grid[y][x]

    # Declare generic parameter for Mapped Callback
    S = TypeVar('S')

    # We map all values from the current Grid which all have type T, to type S
    def map(self, func: Callable[[T], S]) -> Grid[S]:
        return Grid([list(map(func, row)) for row in self.__grid])

    def print(self):
        for row in self.__grid:
            print(row)
