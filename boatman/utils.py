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

"""Utilities."""


import os
import sys


def run(win_cmd: str = '', x_cmd: str = '') -> None:
    """Run OS command, which one depends on the running platform.

    :param win_cmd: windows command to run.
    :param x_cmd: linux command to run.
    """
    assert isinstance(win_cmd, str) and isinstance(x_cmd, str)
    if sys.platform == 'win32':
        os.system(win_cmd)
    else:
        os.system(x_cmd)
