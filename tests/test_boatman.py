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

"""Pytest for boatman."""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__) + '/../boatman')

import boatman
import localization as lcl


def test_upd_status():  # TODO: complete tests
    cur_boat_pos = boatman.RIGHT
    left_items = [' ', ' ', ' ']
    right_items = list(lcl.ITEMS)
    result = boatman.upd_status(cur_boat_pos, left_items, right_items)
    assert result == lcl.GAME_OVER


def test_move_boat():
    to_pos = boatman.LEFT
    result = boatman.move_boat(to_pos)
    assert result == to_pos
    
    to_pos = boatman.RIGHT
    result = boatman.move_boat(to_pos)
    assert result == to_pos


def test_move_left():  # TODO: complete tests
    item = lcl.ITEMS[1]
    boat_pos = boatman.RIGHT
    left_items = [lcl.ITEMS[0], '', '']
    right_items = [''] + list(lcl.ITEMS[1:])
    result = boatman.move_left(item, boat_pos, left_items, right_items)
    assert result in [(None, boatman.LEFT), (None, boatman.RIGHT),
                      (lcl.GAME_OVER, boatman.LEFT),
                      (lcl.GAME_OVER, boatman.RIGHT)]
    

def test_move_right():  # TODO: complete tests
    item = lcl.ITEMS[1]
    boat_pos = boatman.LEFT
    left_items = list(lcl.ITEMS)
    right_items = ['', '', '']
    result = boatman.move_right(item, boat_pos, left_items, right_items)
    assert result in [(None, boatman.LEFT), (None, boatman.RIGHT),
                      (lcl.GAME_OVER, boatman.LEFT),
                      (lcl.GAME_OVER, boatman.RIGHT)]


if __name__ == '__main__':
    pytest.main()
