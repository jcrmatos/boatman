#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2009-2015 Joao Carlos Roseta Matos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

# import io  # Python 3 compatibility
import sys

from builtins import input  # Python 3 compatibility
import colorama as clrm

import ansi
import localization as lcl


ALLOWED_KEYS = lcl.ITEMS + [lcl.QUIT]
BOAT = r'\___/'
NO_BOAT = '     '
DOCK = clrm.Style.BRIGHT + clrm.Fore.YELLOW + '===' + clrm.Style.RESET_ALL
SEA = (clrm.Back.BLUE +
       '                                                   ' +
       clrm.Back.RESET)
# some auxiliary constants to help reading the code
RIGHT = True
LEFT = False


def fireworks():
    """Print fireworks."""
    ansi.print_at(2, 48, clrm.Style.BRIGHT + r'\ | /')
    ansi.print_at(3, 47, '-- * --')
    ansi.print_at(4, 48, '/ | \\')

    ansi.print_at(3, 38, clrm.Fore.RED + r'\ | /')
    ansi.print_at(4, 37, '-- * --')
    ansi.print_at(5, 38, '/ | \\')
    ansi.print_at(4, 28, clrm.Fore.YELLOW + r'\ | /')
    ansi.print_at(5, 27, '-- * --')
    ansi.print_at(6, 28, '/ | \\')

    ansi.print_at(7, 37, clrm.Fore.MAGENTA + '*')
    ansi.print_at(8, 45, clrm.Fore.GREEN + '*')
    ansi.print_at(9, 40, clrm.Fore.CYAN + '*' + clrm.Style.RESET_ALL)


def upd_status(cur_boat_pos, left_items, right_items):
    """Update game status, showing a message and if won some fireworks."""
    if right_items == lcl.ITEMS:  # win
        ansi.print_at(5, 1, lcl.WIN)
        fireworks()
        return lcl.GAME_OVER
    elif ((lcl.WOLF in left_items and
           lcl.GOAT in left_items and
           cur_boat_pos == RIGHT) or
          (lcl.WOLF in right_items and
           lcl.GOAT in right_items and
           cur_boat_pos == LEFT)):  # loss
        ansi.print_at(5, 1, lcl.WOLF_ATE_GOAT)
        return lcl.GAME_OVER
    elif ((lcl.GOAT in left_items and
           lcl.PASTURE in left_items and
           cur_boat_pos == RIGHT) or
          (lcl.GOAT in right_items and
           lcl.PASTURE in right_items and
           cur_boat_pos == LEFT)):  # loss
        ansi.print_at(5, 1, lcl.GOAT_ATE_PASTURE)
        return lcl.GAME_OVER


def move_boat(to_pos):
    """Move boat to right/left dock, and returns position after move."""
    if to_pos == RIGHT:
        for col in range(5, 51):
            ansi.print_at(11, col - 1, NO_BOAT)
            ansi.print_at(11, col, BOAT)
        return RIGHT
    else:
        for col in range(50, 4, -1):
            ansi.print_at(11, col, NO_BOAT)
            ansi.print_at(11, col - 1, BOAT)
        return LEFT


def move_right(item, boat_pos, left_items, right_items):
    """Move item to right dock."""
    pos = lcl.ITEMS.index(item)
    left_items[pos] = ' '
    ansi.print_at(10, 1, clrm.Style.BRIGHT + ''.join(left_items) +
                  clrm.Style.DIM)

    if boat_pos == RIGHT:
        cur_boat_pos = move_boat(LEFT)
        if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
            return lcl.GAME_OVER, cur_boat_pos
    cur_boat_pos = move_boat(RIGHT)

    right_items[pos] = item
    ansi.print_at(10, 55, clrm.Style.BRIGHT + ''.join(right_items) +
                  clrm.Style.DIM)

    if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
        return lcl.GAME_OVER, cur_boat_pos

    return None, cur_boat_pos


def move_left(item, boat_pos, left_items, right_items):
    """Move item to left dock."""
    pos = lcl.ITEMS.index(item)
    right_items[pos] = ' '
    ansi.print_at(10, 55, clrm.Style.BRIGHT + ''.join(right_items) +
                  clrm.Style.DIM)

    if boat_pos == LEFT:
        cur_boat_pos = move_boat(RIGHT)
        if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
            return lcl.GAME_OVER, cur_boat_pos
    cur_boat_pos = move_boat(LEFT)

    left_items[pos] = item
    ansi.print_at(10, 1, clrm.Style.BRIGHT + ''.join(left_items) +
                  clrm.Style.DIM)

    if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
        return lcl.GAME_OVER, cur_boat_pos

    return None, cur_boat_pos


def main():
    """Clear screen, draw scenario, request input and select correct action."""
    left_items = lcl.ITEMS[:]  # left dock items
    right_items = [' ', ' ', ' ']  # right dock items
    cur_boat_pos = LEFT  # current boat position

    clrm.init()
    ansi.clear_screen()

    print(lcl.TITLE)
    ansi.print_at(10, 1, clrm.Style.BRIGHT + ''.join(left_items) +
                  clrm.Style.DIM)
    ansi.print_at(11, 1, DOCK)
    ansi.print_at(11, 4, BOAT)
    ansi.print_at(11, 55, DOCK)
    ansi.print_at(12, 4, SEA)

    while True:
        choice = ''
        while choice not in ALLOWED_KEYS:
            ansi.print_at(14, 1, lcl.PROMPT)
            choice = input('> ').upper()
            # ToDo: check for unicode and clear
            ansi.clear_line(14)  # must clear line before actual input (!?)

        if choice in lcl.ITEMS:
            if choice in left_items:
                result, cur_boat_pos = move_right(choice, cur_boat_pos,
                                                  left_items, right_items)
            else:
                result, cur_boat_pos = move_left(choice, cur_boat_pos,
                                                 left_items, right_items)

            if result == lcl.GAME_OVER:
                ansi.print_at(6, 1, lcl.GAME_OVER)
                break
        else:  # Quit
            break

    ansi.set_print_pos(16, 1)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    sys.exit(main())


# ToDo: add sound
# ToDo: gui version
