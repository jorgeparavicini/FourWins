from typing import Callable

from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtWidgets import QWidget

from bots.botutilities import Grid


class GridRenderer(QWidget):
    bot_1_color = QColor(255, 0, 0)
    bot_2_color = QColor(0, 0, 255)

    def __init__(self, grid: Grid,
                 color_for_bot: Callable[[int], QColor] = lambda a: QColor(255, 0, 0) if a == 1 else QColor(0, 255, 0)):
        super().__init__()
        self.grid = grid
        self.color_for_bot = color_for_bot

    def paintEvent(self, a0: QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp: QPainter):
        self.draw_grid(qp)
        self.draw_cells(qp)

    def draw_grid(self, qp: QPainter):
        for i in range(self.grid.width - 1):
            width = (i + 1) * self.width() / self.grid.width
            qp.drawLine(width, 0, width, self.height())

        for i in range(self.grid.height - 1):
            height = (i + 1) * self.height() / self.grid.height
            qp.drawLine(0, height, self.width(), height)

    def draw_cells(self, qp: QPainter):
        self.grid.print()
        for column in range(self.grid.width):
            for row in range(self.grid.height):
                bot_id = self.grid.at(column, row)
                if bot_id == 0:
                    continue
                else:
                    self.draw_cell_at(column, row, qp, self.color_for_bot(bot_id))

    def center_of_cell(self, x: int, y: int) -> (float, float):
        # We need to invert the y position
        y = (self.grid.height - 1) - y
        return self.cell_size()[0] * (x + 0.5), self.cell_size()[1] * (y + 0.5)

    def draw_cell_at(self, x: int, y: int, qp: QPainter, color: QColor):
        center = self.center_of_cell(x, y)
        center_point = QPointF(center[0], center[1])
        qp.setPen(Qt.NoPen)
        qp.setBrush(color)
        qp.drawEllipse(center_point, self.cell_size()[0] / 2 * 3 / 4, self.cell_size()[1] / 2 * 3 / 4)

    def cell_size(self) -> (int, int):
        return self.width() / self.grid.width, self.height() / self.grid.height
