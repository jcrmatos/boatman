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

"""Localization."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# import io  # Python 3 compatibility
import locale
import sys

# from builtins import input  # Python 3 compatibility
import colorama as clrm


def sys_lang():
    """Get system language."""
    lang = locale.getdefaultlocale()
    # lang = 'EN'  # only for testing
    if 'pt_' in lang[0]:  # Portuguese
        return 'PT'
    else:  # English
        return 'EN'

LANG = sys_lang()

FS_ENC = sys.getfilesystemencoding()
INPUT_ENC = sys.stdin.encoding
UTF_ENC = 'utf-8'

if LANG == 'PT':  # Portuguese
    GAME_OVER = 'Fim do jogo.'
    GOAT = 'C'
    GOAT_ATE_PASTURE = 'A cabra comeu o pasto. Perdeu :('
    ITEMS = ['L', 'C', 'P']
    PASTURE = 'P'
    PROMPT = (clrm.Style.BRIGHT + 'L' + clrm.Style.DIM + '(obo), ' +
              clrm.Style.BRIGHT + 'C' + clrm.Style.DIM + '(abra), ' +
              clrm.Style.BRIGHT + 'P' + clrm.Style.DIM + '(asto), ' +
              clrm.Style.BRIGHT + 'S' + clrm.Style.DIM + '(air)')
    QUIT = 'S'
    TITLE = ('----------------------- ' +
             clrm.Style.BRIGHT + 'Barqueiro' + clrm.Style.DIM +
             ' -----------------------')
    WIN = clrm.Style.BRIGHT + 'Parabéns, ganhou!' + clrm.Style.RESET_ALL
    WOLF = 'L'
    WOLF_ATE_GOAT = 'O lobo comeu a cabra. Perdeu :('
else:  # English
    GAME_OVER = 'Game over.'
    GOAT = 'G'
    GOAT_ATE_PASTURE = 'The goat ate the pasture. You lose :('
    ITEMS = ['W', 'G', 'P']
    PASTURE = 'P'
    PROMPT = (clrm.Style.BRIGHT + 'W' + clrm.Style.DIM + '(olf), ' +
              clrm.Style.BRIGHT + 'G' + clrm.Style.DIM + '(oat), ' +
              clrm.Style.BRIGHT + 'P' + clrm.Style.DIM + '(asture), ' +
              clrm.Style.BRIGHT + 'Q' + clrm.Style.DIM + '(uit)')
    QUIT = 'Q'
    TITLE = ('----------------------- ' +
             clrm.Style.BRIGHT + 'Boatman' + clrm.Style.DIM +
             ' -----------------------')
    WIN = 'Congratulations, you won!'
    WOLF = 'W'
    WOLF_ATE_GOAT = 'The wolf ate the goat. You lose :('


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    pass
