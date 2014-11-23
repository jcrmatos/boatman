#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Localization."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from locale import getdefaultlocale
from colorama import init, Style, Fore, Back


def sys_lang():
    """Get system language."""
    lang = getdefaultlocale()
    #lang = 'EN'  # only for testing
    if 'pt_' in lang[0]:  # Portuguese
        return 'PT'
    else:  # English
        return 'EN'


LANG = sys_lang()
if LANG == 'PT':  # Portuguese
    TITLE = ('----------------------- ' +
             Style.BRIGHT + 'Barqueiro' + Style.DIM +
             ' -----------------------')
    QUIT = 'S'
    ITEMS = ['L', 'C', 'P']
    PROMPT = (Style.BRIGHT + 'L' + Style.DIM + '(obo), ' +
              Style.BRIGHT + 'C' + Style.DIM + '(abra), ' +
              Style.BRIGHT + 'P' + Style.DIM + '(asto), ' +
              Style.BRIGHT + 'S' + Style.DIM + '(air)')
    WOLF = 'L'
    GOAT = 'C'
    PASTURE = 'P'
    WIN = Style.BRIGHT + 'Parabéns, ganhou!' + Style.RESET_ALL
    WOLF_ATE_GOAT = 'O lobo comeu a cabra. Perdeu :('
    GOAT_ATE_PASTURE = 'A cabra comeu o pasto. Perdeu :('
    GAME_OVER = 'Fim do jogo.'
else:  # English
    TITLE = ('----------------------- ' +
             Style.BRIGHT + 'Boatman' + Style.DIM +
             ' -----------------------')
    QUIT = 'Q'
    ITEMS = ['W', 'G', 'P']
    PROMPT = (Style.BRIGHT + 'W' + Style.DIM + '(olf), ' +
              Style.BRIGHT + 'G' + Style.DIM + '(oat), ' +
              Style.BRIGHT + 'P' + Style.DIM + '(asture), ' +
              Style.BRIGHT + 'Q' + Style.DIM + '(uit)')
    WOLF = 'W'
    GOAT = 'G'
    PASTURE = 'P'
    WIN = 'Congratulations, you won!'
    WOLF_ATE_GOAT = 'The wolf ate the goat. You lose :('
    GOAT_ATE_PASTURE = 'The goat ate the pasture. You lose :('
    GAME_OVER = 'Game over.'


if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
    pass
