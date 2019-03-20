import os
import tty
import sys
import termios

level_1 = []


def maze_level_1(level_1, filename):
    with open(filename, 'r') as myfile:
        for character in myfile:
            level_1.append(character.split(' '))



def character_converting(level_1):
    converted_characters = []
    for character in level_1:
        if character == '#':
            character = u'\u2500'
        if character == 'I':
            character = u'\u2502'
        if character == '@':
            character = u'\u1024'  
        if character == '.':
            character = ' '   
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
    character_converting(level_1)
