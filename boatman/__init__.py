#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Initialization."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        #unicode_literals
                        )
# The above unicode_literals import prevents setup.py from working.
# It seems to be a bug in setuptools.
# py2exe build also does not work if it is unremarked.
import sys
from os import path
import glob
import codecs

sys.path.insert(1, path.dirname(__file__))  # add to PYTHONPATH
from localization import LANG


AUTHOR = 'Joao Matos'
EMAIL = 'jcrmatos@gmail.com'
COPYRIGHT = 'Copyright 2014 ' + AUTHOR

NAME = 'boatman'
SCRIPT = NAME + '/' + NAME + '.py'

VERSION = '0.0.0'
CHANGE_LOG_FILE = 'ChangeLog.txt'
if path.isfile(CHANGE_LOG_FILE):  # if file exists
    with open(CHANGE_LOG_FILE) as file_:
        VERSION = file_.readline().split()[0]

LONG_DESC = DESC = ''
README_FILE = 'README.txt'
if path.isfile(README_FILE):  # if file exists
    with codecs.open(README_FILE, encoding='cp1252') as file_:
        LONG_DESC = file_.read()
        DESC = LONG_DESC.split('\n')[3]

LICENSE = 'GNU General Public License v2 or later (GPLv2+)'
URL = 'https://github.com/jcrmatos/Boatman'
KEYWORDS = 'boatman logic'
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Environment :: Console',
               'Environment :: Win32 (MS Windows)',
               'Intended Audience :: End Users/Desktop',
               'Natural Language :: Portuguese',
               'Natural Language :: English',
               'License :: OSI Approved ::' + ' ' + LICENSE,
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Topic :: Games/Entertainment',
               #'Private :: Do Not Upload'  # to prevent PyPI publishing
               ]

##if LANG == 'PT':  # Portuguese
##    USAGE_FILE = 'usage_pt.txt'
##    BANNER_FILE = 'banner_pt.txt'
##else:  # English
##    USAGE_FILE = 'usage.txt'
##    BANNER_FILE = 'banner.txt'

LICENSE_FILE = 'LICENSE.txt'
AUTHORS_FILE = 'AUTHORS.txt'

##DATA_FILES = [USAGE_FILE, LICENSE_FILE, BANNER_FILE, README_FILE, AUTHORS_FILE,
##              CHANGE_LOG_FILE]
DATA_FILES = [LICENSE_FILE, README_FILE, AUTHORS_FILE, CHANGE_LOG_FILE]

#DATA_FILES_PY2EXE = [('', [NAME + '/' + USAGE_FILE]),
#                     ('', [NAME + '/' + BANNER_FILE]),
#                     ('', [NAME + '/' + LICENSE_FILE]),
#                     ('', [NAME + '/' + README_FILE]),
#                     ('', [NAME + '/' + AUTHORS_FILE]),
#                     ('', [NAME + '/' + CHANGE_LOG_FILE])]
DATA_FILES_PY2EXE = glob.glob(NAME + '/' + '*.txt')

#DATA_FILES_CXF = [(NAME + '/' + 'usage.txt', 'usage.txt'),
#                  (NAME + '/' + 'usage_pt.txt', 'usage_pt.txt'),
#                  (NAME + '/' + 'banner.txt', 'banner.txt'),
#                  (NAME + '/' + 'banner_pt.txt', 'banner_pt.txt'),
#                  (NAME + '/' + LICENSE_FILE, LICENSE_FILE),
#                  (NAME + '/' + README_FILE, README_FILE),
#                  (NAME + '/' + AUTHORS_FILE, AUTHORS_FILE),
#                  (NAME + '/' + CHANGE_LOG_FILE, CHANGE_LOG_FILE)]
DATA_FILES_CXF = glob.glob(NAME + '/' + '*.txt')
