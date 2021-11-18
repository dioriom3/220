"""
Name: Michael Diorio
File Name: three_door_game.py
Problem: To create a graphics window that simulates 3 door game.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin, Rectangle, Point, Text
from button import Button


def main():
    win = GraphWin("Three Door Game", 450, 450)

    button1 = Button(Rectangle(Point(40, 150), Point(130, 235)), "Door 1")
    button2 = Button(Rectangle(Point(180, 150), Point(270, 235)), "Door 2")
    button3 = Button(Rectangle(Point(320, 150), Point(410, 235)), "Door 3")

    button1.draw(win)
    button2.draw(win)
    button3.draw(win)

    text = Text(Point(225, 75), "I have a secret door...")
    text2 = Text(Point(225, 430), "Click to choose my door.")

    text.draw(win)
    text2.draw(win)

    doors_list = [button1, button2, button3]
    rand_door = randint(0, 2)
    secret_door = doors_list[rand_door]
    click = win.getMouse()

    if secret_door.is_clicked(click):
        secret_door.color_button("light green")
        text.undraw()
        text2.undraw()
        text12 = Text(Point(225, 75), "Congrats!")
        text12.setTextColor("green")
        text12.draw(win)
        text3 = Text(Point(225, 315), "You win!")
        text3.setTextColor("green")
        text3.draw(win)
    else:
        if button1.is_clicked(click):
            button1.color_button("red")
            text.undraw()
            text2.undraw()
        elif button2.is_clicked(click):
            button2.color_button("red")
            text.undraw()
            text2.undraw()
        elif button3.is_clicked(click):
            button3.color_button("red")
            text.undraw()
            text2.undraw()
    text11 = Text(Point(225, 75), "Sorry, wrong door. You lost!")
    text11.setTextColor("red")
    text11.draw(win)
    text8 = Text(Point(225, 440), "Click to close window.")
    text8.draw(win)
    correct_door = Text(Point(225, 425), "Door " + str(rand_door + 1) + " is the secret door")
    correct_door.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
