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

"""Package initialization file."""


__author__ = 'Joao Carlos Roseta Matos'  # type: str
__license__ = 'GNU General Public License v3 or later (GPLv3+)'  # type: str
__version__ = '0.0.8'  # type: str


import datetime as dt
import os
import sys


NAME = 'boatman'  # type: str
COPYRIGHT = ('Copyright 2009-' + str(dt.date.today().year) + ' '
             + __author__)  # type: str


# add to PYTHONPATH, used by Sphinx doc system
sys.path.insert(1, os.path.dirname(__file__))
