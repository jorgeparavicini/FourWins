from __future__ import annotations

from typing import TypeVar, List, Generic, Callable

T = TypeVar('T')
""" 
GRID LAYOUT

(0,2) (1,2) (2,2)
(0,1) (1,1) (2,1)
(0,0) (1,0) (2,0)
"""


class Grid(Generic[T]):
    def __init__(self, grid: List[List[T]]):
        self.__grid = grid
        if len(grid) > 0 and len(grid[0]) > 0:
            self.__width = len(grid[0])
            self.__height = len(grid)
        else:
            print('\033[93m' + "Grid has invalid size." + '\033[0m')
            
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

    def set_at(self, x: int, y: int, val: T):
        self.__grid[y][x] = val

    # Declare generic parameter for Mapped Callback
    S = TypeVar('S')

    # We map all values from the current Grid which all have type T, to type S
    def map(self, func: Callable[[T], S]) -> Grid[S]:
        return Grid([list(map(func, row)) for row in self.__grid])

    def row(self, at: int) -> List[T]:
        return self.__grid[at]

    def column(self, at: int) -> List[T]:
        return [row[at] for row in self.__grid]

    def is_column_full(self, column: int) -> bool:
        return self.column(column)[-1] is not 0

    def print(self):
        for row in reversed(self.__grid):
            print(row)

    def check_horizontal_group_at(self, bot_id: int, x: int, y: int) -> int:
        assert (0 <= x < self.width)
        if self.at(x, y) != bot_id:
            return 0
        result = 1
        current_x = x
        # go right
        while True:
            if current_x >= self.width - 1:
                break
            current_x += 1
            if self.at(current_x, y) == bot_id:
                result += 1
            else:
                break
        current_x = x
        while True:
            if current_x <= 0:
                break
            current_x -= 1
            if self.at(current_x, y) == bot_id:
                result += 1
            else:
                break
        return result

    def check_vertical_group_at(self, bot_id: int, x: int, y: int) -> int:
        assert 0 <= y < self.height
        if self.at(x, y) != bot_id:
            return 0
        result = 1
        current_y = y

        while True:
            if current_y >= self.height - 1:
                break
            current_y += 1
            if self.at(x, current_y) == bot_id:
                result += 1
            else:
                break

        current_y = y
        while True:
            if current_y <= 0:
                break
            current_y -= 1
            if self.at(x, current_y) == bot_id:
                result += 1
            else:
                break

        return result

    def check_forward_diagonal_group_at(self, bot_id: int, x: int, y: int) -> int:
        assert 0 <= x < self.width
        assert 0 <= y < self.height

        if self.at(x, y) != bot_id:
            return 0
        result = 1
        current_x = x
        current_y = y
        while True:
            if current_y >= self.height - 1 or current_x >= self.width - 1:
                break
            current_x += 1
            current_y += 1
            if self.at(current_x, current_y) == bot_id:
                result += 1
            else:
                break

        current_x = x
        current_y = y

        while True:
            if current_x <= 0 or current_y <= 0:
                break
            current_x -= 1
            current_y -= 1
            if self.at(current_x, current_y) == bot_id:
                result += 1
            else:
                break

        return result

    def check_backward_diagonal_group_at(self, bot_id: int, x: int, y: int) -> int:
        assert 0 <= x < self.width
        assert 0 <= y < self.height

        if self.at(x, y) != bot_id:
            return 0

        result = 1
        current_x = x
        current_y = y

        while True:
            if current_y >= self.height - 1 or current_x <= 0:
                break
            current_x -= 1
            current_y += 1
            if self.at(current_x, current_y) == bot_id:
                result += 1
            else:
                break

        current_y = y
        current_x = x

        while True:
            if current_y <= 0 or current_x >= self.width - 1:
                break
            current_x += 1
            current_y -= 1
            if self.at(current_x, current_y) == bot_id:
                result += 1
            else:
                break
        return result
