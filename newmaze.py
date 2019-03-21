import os
import sys
import readchar


def maze_levels(level_1, filename):
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
                character = u'\u058d'
            if character == '.':
                character = ' '
            converted_characters.append(character)
    for line in converted_characters:
        for character in line:
            print(character, end="")


def movement(level_1):
    x=3
    y=2
    i=0
    for index in level_1:
        if '@' in index:
            y=i
            x=index.index('@')
        i+=1
    if readchar.readkey() == "5":
        if level_1[y - 1][x] != "#":
            level_1[y][x] = "."
            y -= 1
            level_1[y][x] = "@"
            maze_reload(level_1)(level_1)
    if readchar.readkey() == "2":
        if level_1[y + 1][x] != "#":
            level_1[y][x] = "."
            y += 1
            level_1[y][x] = "@"
    if readchar.readkey() == "1":
         if level_1[y][x - 1] != "#":
            level_1[y][x] = "."
            x -= 1
            level_1[y][x] = "@"
    if readchar.readkey() == "3":
        if level_1[y][x + 1] != "#":
            level_1[y][x] = "."
            x += 1
            level_1[y][x] = "@"
    else:
        print("Invalid key")


def main():
    level_1 = []
    maze_levels(level_1, 'levelfirst.txt')
    character_converting(level_1)
    movement(level_1)


if __name__ == '__main__':
    main()
