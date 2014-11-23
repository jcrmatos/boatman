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
from boatman2 import *


def main():
    """Call start."""
    start()


if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
    sys.exit(main())
