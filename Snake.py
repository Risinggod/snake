import copy
import random

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPaintEvent, QPainter, QKeyEvent, QColor, QBrush
from PyQt6.QtWidgets import QLabel, QErrorMessage


class Snake(QLabel):
    def __init__(self, parent=None):
        super(Snake, self).__init__(parent)
        #deffining the locations as varibals
        self.__delta = 10
        self.__number_x = 30
        self.__number_y = 25

        self.__w = self.__number_x * self.__delta
        self.__h = self.__number_y * self.__delta
        self.__field = QRect(0, 0, self.__w, self.__h)

        self.setFixedSize(self.__field.size())

        self.__error_message = QErrorMessage()
        #deffining the collors for the snake, loot, and playing felld
        self.__brush_black = QBrush(QColor("black"))
        self.__brush_yellow = QBrush(QColor("yellow"))
        self.__brush_red = QBrush(QColor("red"))
        self.__brush_green = QBrush(QColor("green"))
        #setting the start location of the snake
        self.__list_of_rects = list()
        self.__list_of_rects.append(QRect(15 * self.__delta, 15 * self.__delta, self.__delta, self.__delta))
        #making the location of the loot landom
        random.seed("debug")
        #random.seed()
        self.__loot = self.generate_loot()

        self.activateWindow()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        # paint background
        painter.setBrush(self.__brush_black)
        painter.drawRect(self.__field)

        # paint snake
        for rect in self.__list_of_rects:
            painter.drawRect(rect)
            painter.fillRect(rect, self.__brush_yellow)

        painter.fillRect(self.__list_of_rects[0], self.__brush_green)

        # paint loot
        painter.setBrush(self.__brush_red)
        painter.drawEllipse(self.__loot)
    #making a mouve event for the snake

    def keyReleaseEvent(self, ev: QKeyEvent) -> None:
        super(Snake, self).keyReleaseEvent(ev)
        #generating the next location of the snake
        next_rect = copy.deepcopy(self.__list_of_rects[0])
        #making the moviement of the snake
        match ev.key():
            case Qt.Key.Key_Left:
                next_rect.translate(- self.__delta, 0)
            case Qt.Key.Key_Right:
                next_rect.translate(self.__delta, 0)
            case Qt.Key.Key_Up:
                next_rect.translate(0, - self.__delta)
            case Qt.Key.Key_Down:
                next_rect.translate(0, self.__delta)
        #checking of the snake is in the playing field
        if not self.__field.contains(next_rect):
            self.__error_message.showMessage("Out of boundary.")
        #checking if the snake biets itself
        for rect in self.__list_of_rects:
            if rect.contains(next_rect):
                self.__error_message.showMessage("Sneak bits itself.")
        #checking if the snake its the froot and if it doues making the snake longer
        if self.__loot.contains(next_rect):
            self.__loot = self.generate_loot()
        else:
            self.__list_of_rects.pop()

        self.__list_of_rects.insert(0, next_rect)

        self.update()
    #funktion to generate the loot on the playing feeld
    def generate_loot(self):
        loot_x = random.randrange(0, self.__number_x) * self.__delta
        loot_y = random.randrange(0, self.__number_y) * self.__delta

        return QRect(loot_x, loot_y, self.__delta, self.__delta)