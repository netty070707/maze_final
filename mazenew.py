'''import os
import tty
import sys
import termios
'''


def maze_level_1(level_1):
    with open('levelfirst.txt', 'r') as myfile:
        for line in myfil
            print(line, end='')
    print(myfile)





'''stuff  = {'wall':  "#",
          'player':  "@",
          'score':  "."}'''

'''x = 6
y = 4'''

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


level_1 = []
maze_level_1(level_1)
