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

"""Localization."""


import locale
# import sys
from typing import Tuple

from colorama import Style


# pt, en, etc.
if locale.getdefaultlocale()[0]:
    LANG = locale.getdefaultlocale()[0][:2]  # type: str
else:
    LANG = 'en'

# FS_ENC = sys.getfilesystemencoding()  # type: str
# INPUT_ENC = sys.stdin.encoding  # type: str
UTF = 'utf-8'  # type: str


def bright(text: str) -> str:
    """Brighten text.

    :param text: text to brighten.
    :returns: brightened text.
    """
    return Style.BRIGHT + text + Style.DIM


if LANG == 'pt':  # Portuguese
    GAME_OVER = 'Fim do jogo.'  # type: str
    GOAT = 'C'  # type: str
    GOAT_ATE_PASTURE = 'A cabra comeu o pasto. Perdeu :('  # type: str
    ITEMS = ('L', 'C', 'P')  # type: Tuple[str, str, str]
    PASTURE = 'P'  # type: str
    PROMPT = (bright('L') + '(obo), ' + bright('C') + '(abra), ' + bright('P')
              + '(asto), ' + bright('S') + '(air)')  # type: str
    QUIT = 'S'  # type: str
    TITLE = ('----------------------- ' + bright('Barqueiro')
             + ' -----------------------')  # type: str
    WIN = Style.BRIGHT + 'Parabéns, ganhou!' + Style.RESET_ALL  # type: str
    WOLF = 'L'  # type: str
    WOLF_ATE_GOAT = 'O lobo comeu a cabra. Perdeu :('  # type: str
else:  # English
    GAME_OVER = 'Game over.'
    GOAT = 'G'
    GOAT_ATE_PASTURE = 'The goat ate the pasture. You lose :('
    ITEMS = ('W', 'G', 'P')
    PASTURE = 'P'
    PROMPT = (bright('W') + '(olf), ' + bright('G') + '(oat), '
              + bright('P') + '(asture), ' + bright('Q')
              + '(uit)')
    QUIT = 'Q'
    TITLE = ('----------------------- ' + bright('Boatman')
             + ' -----------------------')
    WIN = (Style.BRIGHT + 'Congratulations, you won!'
           + Style.RESET_ALL)
    WOLF = 'W'
    WOLF_ATE_GOAT = 'The wolf ate the goat. You lose :('
