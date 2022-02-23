"""
Scott Repik - Repiksh
lab6.py

Take and encode a message using a key.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def vigenere():
    height = 400
    width = 600
    win = GraphWin("Vigenere", width, height)

    text_message = Text(Point(width / 4.5, 40), "Message to encode")
    text_message.draw(win)
    entry_message = Entry(Point(width / 2, 40), 20)
    entry_message.draw(win)
    key_text = Text(Point(width / 4.5, 65), "Key")
    key_text.draw(win)
    entry_key = Entry(Point(width / 2, 65), 20)
    entry_key.draw(win)

    rect_box = Rectangle(Point(width / 2 - 30, height / 2 - 20), Point(width / 2 + 30, height / 2 + 20))
    rect_box.draw(win)
    button_text = Text(Point(width / 2, height / 2), "Encode")
    button_text.draw(win)
    win.getMouse()

    entry_string = entry_message.getText()
    entry_string_upper = entry_string.upper()
    key_string = entry_key.getText()
    key_string_upper = key_string.upper()
    key_string_real = key_string_upper.replace(" ", "")
    entry_string_real = entry_string_upper.replace(" ", "")

    enc_text = []
    for i in range(len(entry_string_real)):
        new_text = (ord(entry_string_real[i]) + (ord(key_string_real[i % len(key_string_real)]))) % 26
        new_text = new_text + ord('A')
        enc_text.append(chr(new_text))

    disp_text = Text(Point(width / 2, height / 1.4), "".join(enc_text))
    disp_text.draw(win)

    rect_box.undraw()
    button_text.undraw()
    disp_text = Text(Point(width / 2, height / 1.5), "New Message:")
    disp_text.draw(win)

    text_close = Text(Point(width / 2, height - 20), "Click to Close")
    text_close.draw(win)
    win.getMouse()
    win.close()
