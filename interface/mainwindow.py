from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QMessageBox, QGroupBox
from PyQt5.QtWidgets import QComboBox, QLineEdit, QSlider
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt

from bots import BaseBot, DummyBot, bot_manager
from bots.botutilities import Grid
from interface import GridRenderer
from interface.tournament_thread import TournamentThread


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Four Wins")

        layout = QHBoxLayout()
        menu = QVBoxLayout()

        self.tournament = None

        # Create UI

        create_new_group = QGroupBox("Create new Game")
        create_new_layout = QVBoxLayout()
        self.bot_1_cb = QComboBox()
        for name in bot_manager.get_all_bot_names():
            self.bot_1_cb.addItem(name)
        self.bot_2_cb = QComboBox()
        for name in bot_manager.get_all_bot_names():
            self.bot_2_cb.addItem(name)

        width_box = QHBoxLayout()
        width_label = QLabel("Width: ")
        self.grid_width = QLineEdit("7")
        self.grid_width.setValidator(QIntValidator(1, 100))
        width_box.addWidget(width_label)
        width_box.addWidget(self.grid_width)

        height_box = QHBoxLayout()
        height_label = QLabel("Height: ")
        self.grid_height = QLineEdit("7")
        self.grid_height.setValidator(QIntValidator(1, 100))
        height_box.addWidget(height_label)
        height_box.addWidget(self.grid_height)

        speed_box = QHBoxLayout()
        self.speed_label = QLabel("Speed: 1")
        self.speed_label.setFixedWidth(60)
        self.speed = QSlider(Qt.Horizontal)
        self.speed.setMinimum(0)
        self.speed.setMaximum(250)
        self.speed.setValue(100)
        self.speed.valueChanged.connect(self.speed_changed)
        speed_box.addWidget(self.speed_label)
        speed_box.addWidget(self.speed)

        create_new_btn = QPushButton("Creat new Game")
        create_new_btn.pressed.connect(self.create_new_game)

        create_new_layout.addWidget(self.bot_1_cb)
        create_new_layout.addWidget(self.bot_2_cb)
        create_new_layout.addLayout(width_box)
        create_new_layout.addLayout(height_box)
        create_new_layout.addLayout(speed_box)
        create_new_layout.addWidget(create_new_btn)
        create_new_group.setLayout(create_new_layout)

        # Current Game

        current_game_group = QGroupBox("Current Game")
        current_game_layout = QVBoxLayout()
        self.turn_label = QLabel("Turn: 0")
        current_game_layout.addWidget(self.turn_label)

        self.bot_1_label = QLabel(f"Bot 1: {self.bot_1_cb.currentText()}, {self.bot_1_cb.currentText()}")
        self.bot_1_label.setStyleSheet("background-color:#00ff00;")
        current_game_layout.addWidget(self.bot_1_label)

        self.bot_2_label = QLabel(f"Bot 2: {self.bot_2_cb.currentText()}, {self.bot_2_cb.currentText()}")
        self.bot_2_label.setStyleSheet("background-color:#ff0000")
        current_game_layout.addWidget(self.bot_2_label)

        self.button = QPushButton("Start Game")
        self.button.pressed.connect(self.toggle_play)
        self.button.setDisabled(True)
        current_game_layout.addWidget(self.button)

        current_game_layout.addStretch()

        self.renderer = GridRenderer(Grid.empty())

        # Apply Layout
        current_game_group.setLayout(current_game_layout)
        menu.addWidget(create_new_group)
        menu.addWidget(current_game_group)
        layout.addLayout(menu)
        layout.addWidget(self.renderer)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update_bot_names(self):
        self.bot_1_label.setText(f"Bot 1: {self.bot_1_cb.currentText()}")
        self.bot_2_label.setText(f"Bot 2: {self.bot_2_cb.currentText()}")

    def create_tournament_master(self) -> TournamentThread:
        return TournamentThread(bot_manager.get_bot_with_name(self.bot_1_cb.currentText())(1),
                                bot_manager.get_bot_with_name(self.bot_2_cb.currentText())(2),
                                int(self.grid_width.text()), int(self.grid_height.text()),
                                float(self.speed.value() / 100.0))

    def set_new_tournament_master(self, master: TournamentThread):
        self.tournament = master
        self.button.setDisabled(False)
        self.button.setText("Start Game")
        self.renderer.grid = self.tournament.tournament_master.grid
        self.tournament.turn_ended.connect(self.turn_ended)
        self.tournament.winner_found.connect(self.winner_found)
        self.tournament.did_start.connect(self.did_start)
        self.tournament.did_toggle_pause.connect(self.did_toggle_play)
        self.renderer.update()
        self.update_bot_names()

    def create_new_game(self):
        if self.tournament is not None and not self.tournament.is_done:
            msg = QMessageBox()
            result = msg.question(self, "", "The Previous game has not finished yet. Do you want to terminate it?",
                                  msg.Yes | msg.No)
            if result == msg.No:
                return
        if self.tournament is not None:
            self.tournament.stop()
        self.set_new_tournament_master(self.create_tournament_master())

    def toggle_play(self):
        if self.tournament.is_done:
            self.tournament = self.create_tournament_master()
        self.tournament.toggle_pause()

    def turn_ended(self, bot: BaseBot):
        self.turn_label.setText("Turn: " + str(self.tournament.tournament_master.turn))
        self.renderer.update()

    def winner_found(self, bot: BaseBot):
        self.button.setText(f"{bot.name} {bot.id} won")
        self.button.setDisabled(True)
        msg = QMessageBox()
        msg.setText(f"Bot {bot.name} {bot.id} won the game")
        msg.exec_()

    def did_start(self):
        self.button.setText("Pause!")

    def did_toggle_play(self):
        if self.tournament.tournament_master.is_paused:
            self.button.setText("Resume!")
        else:
            self.button.setText("Pause!")

    def speed_changed(self, val):
        self.speed_label.setText(f"Speed: {val / 100.0} - ")
        if self.tournament is not None:
            self.tournament.tournament_master.time_between_rounds = val / 100.0

