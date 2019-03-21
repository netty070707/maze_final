import os
import tty
import readchar
import sys
import termios

level_1 = []


def maze_level_1(level_1, filename):
    with open(filename, 'r') as myfile:
        for line in myfile:
            level_1.append(line.split(' '))


def character_converting(level_1):
    converted_characters = []
    for line in level_1:
        for character in line:
            if character == '#':
                character = u'\u2500'
            if character == 'I':
                character = u'\u2502'
            if character == '@':
                character = u'\u1024'
            if character == '.':
                character = ' '
            converted_characters.append(character)
    for line in converted_characters:
        for character in line:
            print(character, end="")


def readKey():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
    pressedKey = readKey()
    if pressedKey == "w":
        if level_1[0][y - 1][x] != "#":
            level_1[0][y][x] = "."
            y -= 1
            level_1[0][y][x] = "@"
    if pressedKey == "s":
        if level_1[0][y + 1][x] != "#":
            level_1[0][y][x] = "."
            y += 1
            level_1[0][y][x] = "@"
    if pressedKey == "a":
        if level_1[0][y][x - 1] != "#":
            level_1[0][y][x] = "."
            x -= 1
            level_1[0][y][x] = "@"
    if pressedKey == "d":
        if level_1[0][y][x + 1] != "#":
            level_1[0][y][x] = "."
            x += 1
            level_1[0][y][x] = "@"
    if pressedKey == "q" or y == 9 and x == 14:
        break


if __name__ == '__main__':
    maze_level_1(level_1, 'level_third.txt')
    character_converting(level_1)
    readKey()
