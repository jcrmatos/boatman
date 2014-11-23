#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Shared constants and functions."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import os


SYS_VERSION = int(sys.version[0])


def run(win_cmd='', x_cmd=''):
    """Run OS command."""
    if sys.platform == 'win32':
        os.system(win_cmd)
    else:
        os.system(x_cmd)


def clear_screen():
    """Clear screen."""
    #print("\x1b[2J")  # doesn't work :(
    run('cls', 'clear')


def set_print_pos(line, col):
    """Define priting position. Requires colorama."""
    print("\x1b[%d;%dH" % (line, col))


def print_at(line, col, text):
    """Print at line and column. Requires colorama."""
    print("\x1b[%d;%dH%s" % (line, col, text))


def clear_line(line):
    """Clear line."""
    set_print_pos(line, 1)
    #print("\x1b[K")  # doesn't work :(
    print('                                                                   ')
    set_print_pos(line, 1)


if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
    pass
