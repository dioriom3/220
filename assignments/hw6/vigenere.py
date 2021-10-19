"""
Name: Michael Diorio
File Name: vigenere.py

Problem: To implement the vigenere cipher using graphics and string processing.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Point, Text, Entry, Rectangle


def code(message, keyword):
    message = message.upper()
    message = message.replace(" ", "")
    keyword = keyword.upper()
    keyword = keyword.replace(" ", "")

    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    acc = ""
    for i in range(len(message)):
        cip = message[i]
        ky = keyword[i % len(keyword)]
        cip = ord(cip) - 65
        ky = ord(ky) - 65
        x = (cip + ky) % 26
        x_return = x + 65
        char = chr(x_return)
        acc = acc + char
    return acc


def main():
    width = 500
    height = 450
    win = GraphWin("Vigenere", width, height)

    inst_pt = Point(90, 100)
    instructions = Text(inst_pt, "Message to Encode:")
    instructions.draw(win)

    inst_pt = Point(109, 145)
    instructions = Text(inst_pt, "Enter Keyword:")
    instructions.draw(win)

    message_box = Entry(Point(300, 100), 28)
    message_box.setTextColor("blue")
    message_box.draw(win)
    keyword_box = Entry(Point(264, 145), 20)
    keyword_box.setTextColor("purple")
    keyword_box.draw(win)

    button_shape = Rectangle(Point(180, 195), Point(315, 275))
    button_shape.setFill("red")
    button_shape.draw(win)
    button_center = button_shape.getCenter()
    button_message = Text(button_center, "Click to Encode")
    button_message.setTextColor("blue")
    button_message.draw(win)

    win.getMouse()
    button_shape.undraw()
    button_message.undraw()

    message = message_box.getText()
    keyword = keyword_box.getText()

    result_msg = Text(Point(250, 245), "Resulting Message: ")
    result_msg.draw(win)

    encrypt_msg = Text(Point(width / 2, 265), code(message, keyword))
    encrypt_msg.draw(win)

    close_window = Text(Point(width / 2, height - 10), "Click to close.")
    close_window.setTextColor("purple")
    close_window.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
