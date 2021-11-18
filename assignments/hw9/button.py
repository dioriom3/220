"""
Name: Michael Diorio
File Name: button.py
Problem: To encapsulate data for a button shown in a GUI.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from graphics import Text


class Button:
    """sets up button mechanics for the main function"""
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.label

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        return bool(self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX()
                    and self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY())

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
