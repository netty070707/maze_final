import os
import tty
import sys
import termios

level_1 = []


def maze_level_1(level_1, filename):
    with open(filename, 'r') as myfile:
        for line in myfile:
            level_1.append(line)
            print(line, end='')


def character_converting():
    converted_characters = []
    for character in level_1:
        if character == '2':
            character == u'\u2501'
        if character == 'I':
            character == u'\u258f'
        if character == '@':
            character == u'\u258f'  
        if character == '.':
            character == u'\u258f'   
        converted_characters.append(character)
        print(converted_characters)


'''def gameplace():
    for i in level_1:
        print()
        for j in i:
            print(" ".join(j),end='')'''

'''os.system("clear")'''


'''def readKey():
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
        if level_1[y - 1][x] != "#":
            level_1[y][x] = "."
            y -= 1
            level_1[y][x] = "@"
    if pressedKey == "s":
        if level_1[y + 1][x] != "#":
            level_1[y][x] = "."
            y += 1
            level_1[y][x] = "@"
    if pressedKey == "a":
        if level_1[y][x - 1] != "#":
            level_1[y][x] = "."
            x -= 1
            level_1[y][x] = "@"
    if pressedKey == "d":
        if level_1[y][x + 1] != "#":
            level_1[y][x] = "."
            x += 1
            level_1[y][x] = "@"
    if pressedKey == "q" or y == 9 and x == 14:
        break
'''
'''os.system("clear")'''


if __name__ == '__main__':   
    maze_level_1(level_1, 'levelfirst.txt')
    character_converting()
