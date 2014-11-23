#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple logic game.
A boatman is comissioned to take a Wolf, a Goat and some Pasture to the other
margin.
He can only take one at the time.
While he is on the dock, nothing happens.
As soon as he leaves, the animals will try to eat.
The order of transportation is important because the Wolf eats the Goat and
the Goat eats the Pasture, but the Wolf doesn't eat the Pasture.

Portuguese
Um jogo de lógica simples.
Um barqueiro é contratado para levar um Lobo, uma Cabra e Pasto para a outra
margem.
Só pode levar um de cada vez.
Enquanto está na doca nada acontece.
Assim que saí, os animais tentam comer.
A ordem de transporte é importante porque o Lobo come a Cabra e a Cabra come o
Pasto, mas o Lobo não come o Pasto.
"""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
from colorama import init, Style, Fore, Back
from localization import *
from shared import *


ALLOWED_KEYS = ITEMS + list(QUIT)
BOAT = "\___/"
NO_BOAT = '     '
DOCK = Style.BRIGHT + Fore.YELLOW + '===' + Style.RESET_ALL
SEA = (Back.BLUE +
       '                                                   ' +
       Back.RESET)
# some auxiliary constants to help reading the code
RIGHT = True
LEFT = False


def fireworks():
    """Print fireworks."""
    print_at(2, 48, Style.BRIGHT + "\ | /")
    print_at(3, 47, '-- * --')
    print_at(4, 48, '/ | \\')

    print_at(3, 38, Fore.RED + "\ | /")
    print_at(4, 37, '-- * --')
    print_at(5, 38, '/ | \\')
    print_at(4, 28, Fore.YELLOW + "\ | /")
    print_at(5, 27, '-- * --')
    print_at(6, 28, '/ | \\')

    print_at(7, 37, Fore.MAGENTA + '*')
    print_at(8, 45, Fore.GREEN + '*')
    print_at(9, 40, Fore.CYAN + '*' + Style.RESET_ALL)


def update_status(cur_boat_pos, left_items, right_items):
    """Update game status, showing a message and if won some fireworks."""
    if right_items == ITEMS:  # win
        print_at(5, 1, WIN)
        fireworks()
        return GAME_OVER
    elif ((WOLF in left_items and
           GOAT in left_items and
           cur_boat_pos == RIGHT) or
          (WOLF in right_items and
           GOAT in right_items and
           cur_boat_pos == LEFT)):  # loss
        print_at(5, 1, WOLF_ATE_GOAT)
        return GAME_OVER
    elif ((GOAT in left_items and
           PASTURE in left_items and
           cur_boat_pos == RIGHT) or
          (GOAT in right_items and
           PASTURE in right_items and
           cur_boat_pos == LEFT)):  # loss
        print_at(5, 1, GOAT_ATE_PASTURE)
        return GAME_OVER


def move_boat(to_pos):
    """Move boat to right/left dock, and returns position after move."""
    if to_pos == RIGHT:
        for col in range(5, 51):
            print_at(11, col - 1, NO_BOAT)
            print_at(11, col, BOAT)
        return RIGHT
    else:
        for col in range(50, 4, -1):
            print_at(11, col, NO_BOAT)
            print_at(11, col - 1, BOAT)
        return LEFT


def move_right(item, boat_pos, left_items, right_items):
    """Move item to right dock."""
    pos = ITEMS.index(item)
    left_items[pos] = ' '
    print_at(10, 1, Style.BRIGHT + ''.join(left_items) + Style.DIM)

    if boat_pos == RIGHT:
        cur_boat_pos = move_boat(LEFT)
        if update_status(cur_boat_pos, left_items, right_items) == GAME_OVER:
            return GAME_OVER, cur_boat_pos
    cur_boat_pos = move_boat(RIGHT)

    right_items[pos] = item
    print_at(10, 55, Style.BRIGHT + ''.join(right_items) + Style.DIM)

    if update_status(cur_boat_pos, left_items, right_items) == GAME_OVER:
        return GAME_OVER, cur_boat_pos

    return None, cur_boat_pos


def move_left(item, boat_pos, left_items, right_items):
    """Move item to left dock."""
    pos = ITEMS.index(item)
    right_items[pos] = ' '
    print_at(10, 55, Style.BRIGHT + ''.join(right_items) + Style.DIM)

    if boat_pos == LEFT:
        cur_boat_pos = move_boat(RIGHT)
        if update_status(cur_boat_pos, left_items, right_items) == GAME_OVER:
            return GAME_OVER, cur_boat_pos
    cur_boat_pos = move_boat(LEFT)

    left_items[pos] = item
    print_at(10, 1, Style.BRIGHT + ''.join(left_items) + Style.DIM)

    if update_status(cur_boat_pos, left_items, right_items) == GAME_OVER:
        return GAME_OVER, cur_boat_pos

    return None, cur_boat_pos


def start():
    """Clear screen, draw scenario, request input and select correct action."""
    left_items = ITEMS[:]  # left dock items
    right_items = [' ', ' ', ' ']  # right dock items
    cur_boat_pos = LEFT  # current boat position

    init()  # colorama.init()
    clear_screen()

    print(TITLE)
    print_at(10, 1, Style.BRIGHT + ''.join(left_items) + Style.DIM)
    print_at(11, 1, DOCK)
    print_at(11, 4, BOAT)
    print_at(11, 55, DOCK)
    print_at(12, 4, SEA)

    while True:
        choice = ''
        while choice not in ALLOWED_KEYS:
            print_at(14, 1, PROMPT)
            if SYS_VERSION < 3:
                choice = raw_input('> ').upper()
            else:
                choice = input('> ').upper()
            #ToDo: check for unicode and clear
            clear_line(14)  # must clear line before actual input, strange...

        if choice in ITEMS:
            if choice in left_items:
                result, cur_boat_pos = move_right(choice, cur_boat_pos,
                                                  left_items, right_items)
            else:
                result, cur_boat_pos = move_left(choice, cur_boat_pos,
                                                 left_items, right_items)

            if result == GAME_OVER:
                print_at(6, 1, GAME_OVER)
                break
        else:  # Quit
            break

    set_print_pos(16, 1)


if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
    pass
