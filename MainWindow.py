
from PyQt6.QtWidgets import QMainWindow
from Snake import Snake

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Text für die Titelleiste des QMainWinows
        self.setWindowTitle("Snake")

        # Setzt die Größe des Fensters auf feste Werte
        # self.setFixedWidth(800)
        # self.setFixedHeight(600)

       # self.setMinimumWidth(200)
        #self.setMinimumHeight(200)

       # self.setMaximumWidth(200)
       # self.setMaximumHeight(200)

        snake = Snake(self)
        self.setCentralWidget(snake)

        self.setStyleSheet("background-color : black;")