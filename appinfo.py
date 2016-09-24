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

"""Application basic information."""

from typing import List

import boatman


APP_NAME = boatman.__name__  # type: str
APP_VERSION = boatman.__version__  # type: str
APP_LICENSE = boatman.__license__  # type: str
APP_AUTHOR = boatman.__author__  # type: str
APP_EMAIL = 'jcrmatos@gmail.com'  # type: str
APP_URL = 'https://github.com/jcrmatos/boatman'  # type: str
APP_KEYWORDS = 'boat man'  # type: str

# change classifiers to be correct for your application/module
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = ('Development Status :: 5 - Production/Stable',
               'Environment :: Console',
               'Intended Audience :: End Users/Desktop',
               'License :: OSI Approved :: ' + APP_LICENSE,
               'Natural Language :: English',
               'Natural Language :: Portuguese',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3 :: Only',
               'Topic :: Games/Entertainment'
)  # type: Tuple[str]

COPYRIGHT = boatman.COPYRIGHT  # type: str

README_FILE = 'README.rst'  # type: str
REQUIREMENTS_FILE = 'requirements.txt'  # type: str
REQUIREMENTS_DEV_FILE = 'requirements-dev.txt'  # type: str
