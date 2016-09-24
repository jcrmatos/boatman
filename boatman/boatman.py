#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2009-2016 Joao Carlos Roseta Matos
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


from time import sleep
from typing import Dict, List, Optional, Tuple

from colorama import init, Style, Fore, Back

from ansi_helper import clear_screen, set_print_pos, print_at, clear_line
import localization as lcl


ALLOWED_KEYS = lcl.ITEMS + (lcl.QUIT,)  # type: Tuple[str, str, str, str]
BOAT = r'\___/'  # type: str
NO_BOAT = ' ' * len(BOAT)  # type: str
DOCK = Style.BRIGHT + Fore.YELLOW + '===' + Style.RESET_ALL  # type: str
SEA = (Back.BLUE + ' ' * 51 + Back.RESET)  # type: str
RIGHT = True  # type: bool
LEFT = False  # type: bool


def fireworks() -> None:
    """Print fireworks."""
    print_at(2, 48, Style.BRIGHT + r'\ | /')
    print_at(3, 47, '-- * --')
    print_at(4, 48, '/ | \\')

    print_at(3, 38, Fore.RED + r'\ | /')
    print_at(4, 37, '-- * --')
    print_at(5, 38, '/ | \\')
    print_at(4, 28, Fore.YELLOW + r'\ | /')
    print_at(5, 27, '-- * --')
    print_at(6, 28, '/ | \\')

    print_at(7, 37, Fore.MAGENTA + '*')
    print_at(8, 45, Fore.GREEN + '*')
    print_at(9, 40, Fore.CYAN + '*' + Style.RESET_ALL)


def upd_status(cur_boat_pos: bool, left_items: List[str],
               right_items: List[str]) -> Optional[str]:
    """Update game status, showing a message and if won some fireworks.

    :param cur_boat_pos: current boat position (LEFT=False, RIGHT=True).
    :param left_items: items in left dock.
    :param right_items: items in right dock.
    :returns: None or localized game over message.
    """
    assert all([isinstance(cur_boat_pos, bool), isinstance(left_items, list),
                isinstance(right_items, list)])

    conditions = {
        'win': right_items == list(lcl.ITEMS),
        'wolf_ate_goat':
            all([lcl.WOLF in left_items, lcl.GOAT in left_items,
                 cur_boat_pos == RIGHT])
            or
            all([lcl.WOLF in right_items, lcl.GOAT in right_items,
                 cur_boat_pos == LEFT]),
        'goat_ate_pasture':
            all([lcl.GOAT in left_items, lcl.PASTURE in left_items,
                 cur_boat_pos == RIGHT])
            or
            all([lcl.GOAT in right_items, lcl.PASTURE in right_items,
                 cur_boat_pos == LEFT])
    }  # type: Dict[str, bool]

    if conditions['win']:
        print_at(5, 1, lcl.WIN)
        fireworks()
        return lcl.GAME_OVER
    elif conditions['wolf_ate_goat']:  # loss
        print_at(5, 1, lcl.WOLF_ATE_GOAT)
        return lcl.GAME_OVER
    elif conditions['goat_ate_pasture']:  # loss
        print_at(5, 1, lcl.GOAT_ATE_PASTURE)
        return lcl.GAME_OVER


def bright(items: List[str]) -> str:
    """Brighten and concatenate items.

    :param items: items to brighten.
    :returns: brightened and concatenated items.
    """
    return Style.BRIGHT + ''.join(items) + Style.DIM


def move_boat(to_pos: bool) -> bool:
    """Move boat to right/left dock, and returns position after move.

    :param to_pos: position to move boat to (LEFT=False, RIGHT=True).
    :returns: boat's current position.
    """
    assert isinstance(to_pos, bool)
    if to_pos == RIGHT:
        for col in range(5, 51):  # type: int
            print_at(11, col - 1, NO_BOAT)
            print_at(11, col, BOAT)
            sleep(.02)
    else:
        for col in range(50, 4, -1):  # type: int
            print_at(11, col, NO_BOAT)
            print_at(11, col - 1, BOAT)
            sleep(.02)
    return to_pos


def move_right(item: str, boat_pos: bool, left_items: List[str],
               right_items: List[str]) -> Tuple[Optional[str], bool]:
    """Move item to right dock.

    :param item: item to move.
    :param boat_pos: current boat position (LEFT=False, RIGHT=True).
    :param left_items: items in left dock.
    :param right_items: items in right dock.
    :returns: (None, curr. boat pos) or (loc. game over msg, curr. boat pos).
    """
    assert all([isinstance(item, str), isinstance(boat_pos, bool),
                isinstance(left_items, list), isinstance(right_items, list)])
    if boat_pos == RIGHT:
        cur_boat_pos = move_boat(LEFT)  # type: bool
        if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
            return lcl.GAME_OVER, cur_boat_pos

    pos = lcl.ITEMS.index(item)  # type: int
    left_items[pos] = ' '
    print_at(10, 1, bright(left_items))

    cur_boat_pos = move_boat(RIGHT)

    right_items[pos] = item
    print_at(10, 55, bright(right_items))

    if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
        return lcl.GAME_OVER, cur_boat_pos

    return None, cur_boat_pos


def move_left(item: str, boat_pos: bool, left_items: List[str],
              right_items: List[str]) -> Tuple[Optional[str], bool]:
    """Move item to left dock.

    :param item: item to move.
    :param boat_pos: current boat position (LEFT=False, RIGHT=True).
    :param left_items: items in left dock.
    :param right_items: items in right dock.
    :returns: (None, curr. boat pos) or (loc. game over msg, curr. boat pos).
    """
    assert all([isinstance(item, str), isinstance(boat_pos, bool),
                isinstance(left_items, list), isinstance(right_items, list)])
    if boat_pos == LEFT:
        cur_boat_pos = move_boat(RIGHT)  # type: bool
        if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
            return lcl.GAME_OVER, cur_boat_pos

    pos = lcl.ITEMS.index(item)  # type: int
    right_items[pos] = ' '
    print_at(10, 55, bright(right_items))

    cur_boat_pos = move_boat(LEFT)

    left_items[pos] = item
    print_at(10, 1, bright(left_items))

    if upd_status(cur_boat_pos, left_items, right_items) == lcl.GAME_OVER:
        return lcl.GAME_OVER, cur_boat_pos

    return None, cur_boat_pos


def draw_scenery(left_items: List[str]):
    """Draw scenery.

    :param left_items: items in left dock.
    """
    print(lcl.TITLE)
    print_at(10, 1, bright(left_items))
    print_at(11, 1, DOCK)
    print_at(11, 4, BOAT)
    print_at(11, 55, DOCK)
    print_at(12, 4, SEA)


def main() -> None:
    """Clear screen, draw scenario, request input and select correct action."""
    # left dock items
    left_items = list(lcl.ITEMS)  # type: List[str]
    # right dock items
    right_items = [' ', ' ', ' ']  # type: List[str]
    # current boat position
    cur_boat_pos = LEFT  # type: bool

    init()
    clear_screen()

    draw_scenery(left_items)

    while True:
        choice = ''  # type: str
        while choice not in ALLOWED_KEYS:
            print_at(14, 1, lcl.PROMPT)
            choice = input('> ').upper()
            clear_line(14)

        if choice in lcl.ITEMS:
            result = None  # type: Optional[str]
            if choice in left_items:
                result, cur_boat_pos = move_right(choice, cur_boat_pos,
                                                  left_items, right_items)
            else:
                result, cur_boat_pos = move_left(choice, cur_boat_pos,
                                                 left_items, right_items)

            if result == lcl.GAME_OVER:
                print_at(6, 1, lcl.GAME_OVER)
                break
        else:  # Quit
            break

    set_print_pos(16, 1)


if __name__ == '__main__':
    main()


# ToDo: add sound
# ToDo: gui version
