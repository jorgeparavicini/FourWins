from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from bots import BaseBot
from interface import GridRenderer
from interface.tournament_thread import TournamentThread


class MainWindow(QMainWindow):
    def __init__(self, bot_1: BaseBot, bot_2: BaseBot, width: int, height: int, time: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Four Wins")

        self.tournament = TournamentThread(bot_1, bot_2, width, height, time)
        self.tournament.turn_ended.connect(self.turn_ended)
        self.tournament.winner_found.connect(self.winner_found)

        layout = QHBoxLayout()
        menu_layout = QVBoxLayout()

        self.turn_label = QLabel("Turn: 0")
        menu_layout.addWidget(self.turn_label)

        self.bot_1_label = QLabel(f"Bot 1: {bot_1.name}, {bot_1.id}")
        self.bot_1_label.setStyleSheet("background-color:#00ff00;")
        menu_layout.addWidget(self.bot_1_label)

        self.bot_2_label = QLabel(f"Bot 2: {bot_2.name}, {bot_1.id}")
        self.bot_2_label.setStyleSheet("background-color:#ff00ff")
        menu_layout.addWidget(self.bot_2_label)

        self.button = QPushButton("Start Game")
        self.button.pressed.connect(self.start_game)
        menu_layout.addWidget(self.button)

        menu_layout.addStretch()

        self.renderer = GridRenderer(self.tournament.tournament_master.grid)

        # Apply Layout
        layout.addLayout(menu_layout)
        layout.addWidget(self.renderer)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def start_game(self):
        self.tournament.start()

    def turn_ended(self, bot: BaseBot):
        self.turn_label.setText("Turn: " + str(self.tournament.tournament_master.turn))
        self.renderer.update()

    def winner_found(self, bot: BaseBot):
        print("Winner found")
