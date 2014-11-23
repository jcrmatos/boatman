#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Utils library."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import os
import codecs


def py_app_ver():
    """
    Write Python and application version (from ChangeLog.rst) to text files.
    """
    py_ver = sys.version.split()[0]
    py_ver = py_ver.split('.')
    py_ver = str(py_ver[0] + '.' + py_ver[1])

    with open('ChangeLog.rst') as file_:
        app_ver = file_.readline().split()[0]

    with open('py_ver.txt', 'w') as file_:
        file_.write(py_ver)

    with open('app_ver.txt', 'w') as file_:
        file_.write(app_ver)


def prep_rst2pdf():
    """Remove parts of rST to create a better pdf."""
    with open('doc/index.ori') as file_:
        text = file_.readlines()

    new_text = ''

    for line in text:
        if 'Contents:' in line:
            pass
        elif 'Indices and tables' in line:
            break
        else:
            new_text += line

    with open('doc/index.rst', 'w') as file_:
        file_.writelines(new_text)


def project_name():
    """Get project name from environment variable."""
    return os.getenv('PROJECT')


def docstr2readme():
    """Copy main module docstring to README.rst."""
    project = project_name()

    with codecs.open(project + '/' + project + '.py',
                     encoding='utf8') as file_:
        text = file_.readlines()

    text2copy = project + '\n' + '=' * len(project) + '\n\n'

    start_copy = False

    for line in text:
        if '"""' in line:
            if start_copy:
                break
            else:
                start_copy = True
        elif start_copy:
            text2copy += line

    text2copy += '\n'

    with codecs.open('README.rst', encoding='cp1252') as file_:
        text = file_.readlines()

    until_eof = False

    for line in text:
        if 'Resources' in line or until_eof:
            text2copy += line
            until_eof = True

    with codecs.open('README.rst', 'wb', encoding='cp1252') as file_:
        file_.writelines(text2copy)


if __name__ == '__main__':
    eval(sys.argv[1])
