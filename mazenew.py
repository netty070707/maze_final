import os
import tty, sys, termios

with open("level_first.txt", "r") as level1:
    level1.readlines()
    level1.read().split(',')
    print(level1)

stuff  = {'wall'  :  "#",
          'player':  "@",
          'empty' :  "."}

x=6
y=4

def gameplace():
    for i in level1:
        print()
        for j in i:
            print(" ".join(j),end='')

os.system("clear")
gameplace()
print()


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
    print()
        
    if pressedKey=="w":
        if level1[y-1][x]!="#":
            level1[y][x]="."
            y -=1
            level1[y][x]="@"   
    if pressedKey=="s":
        if level1[y+1][x]!="#":
            level1[y][x]="."
            y +=1
            level1[y][x]="@"
    if pressedKey=="a":
        if level1[y][x-1]!="#":
            level1[y][x]="."
            x -=1
            level1[y][x]="@"
    if pressedKey=="d":
        if level1[y][x+1]!="#":
            level1[y][x]="."
            x +=1
            level1[y][x]="@"
    if pressedKey=="q" or y==9 and x==14:
        break

    os.system("clear")
   
    gameplace()
    print()
