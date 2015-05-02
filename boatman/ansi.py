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

"""ANSI helper functions."""

# Python 3 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# import builtins  # Python 3 compatibility
# import future  # Python 3 compatibility
# import io  # Python 3 compatibility

import utils


def clear_screen():
    """Clear screen."""
    # print('\x1b[2J')  # doesn't work :(
    utils.run('cls', 'clear')


def set_print_pos(line, col):
    """Define priting position. Requires colorama."""
    print('\x1b[%d;%dH' % (line, col))


def print_at(line, col, text):
    """Print at line and column. Requires colorama."""
    print('\x1b[%d;%dH%s' % (line, col, text))


def clear_line(line):
    """Clear line."""
    set_print_pos(line, 1)
    # print('\x1b[K')  # doesn't work :(
    print('                                                                 ' +
          '  ')
    set_print_pos(line, 1)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    pass
