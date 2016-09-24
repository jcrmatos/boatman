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

"""ANSI helper functions (requires colorama)."""


import utils


def clear_screen() -> None:
    """Clear screen."""
    # print('\x1b[2J')  # doesn't work :(
    utils.run('cls', 'clear')


def set_print_pos(line: int, col: int) -> None:
    """Define priting position (requires colorama).

    :param line: line number to position cursor.
    :param col: column number to position cursor.
    """
    assert all([isinstance(line, int), 1 <= line <= 25,
                isinstance(col, int), 1 <= line <= 80])
    print('\x1b[%d;%dH' % (line, col))


def print_at(line: int, col: int, text: str) -> None:
    """Print text at line and column (requires colorama).

    :param line: line number where to print.
    :param col: column number where to print.
    :param text: text to print.
    """
    assert all([isinstance(line, int), 1 <= line <= 25,
                isinstance(col, int), 1 <= line <= 80,
                isinstance(text, str)])
    print('\x1b[%d;%dH%s' % (line, col, text))


def clear_line(line: int) -> None:
    """Clear line.

    :param line: line number to clear.
    """
    assert isinstance(line, int) and (1 <= line <= 25)
    set_print_pos(line, 1)
    # print('\x1b[K')  # doesn't work :(
    print(' ' * 80)
    set_print_pos(line, 1)
