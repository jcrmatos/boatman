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

"""Setup for source, egg, wheel, wininst, msi and dumb distributions."""

import io
import os
from typing import Dict, List

from setuptools import setup, find_packages

from appinfo import (APP_AUTHOR, APP_EMAIL, APP_KEYWORDS, APP_LICENSE,
                     APP_NAME, APP_URL, APP_VERSION, CLASSIFIERS, README_FILE,
                     REQUIREMENTS_FILE, REQUIREMENTS_DEV_FILE)


UTF = 'utf-8'  # type: str


def get_deps_names(filename: str) -> List[str]:
    """Extract dependencies names from requirements file.
    
    :param filename: requirements filename.
    :return: list of dependencies names.
    """
    deps = ['']  # type: List[str]
    if os.path.isfile(filename):
        with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            deps = f_in.read().splitlines()
            for idx, line in enumerate(deps):  # type: int, str
                if '<' in line:
                    deps[idx] = line.split('<')[0].strip()
                elif '>' in line:
                    deps[idx] = line.split('>')[0].strip()
                elif '=' in line:
                    deps[idx] = line.split('=')[0].strip()
            deps = [line for line in deps if line and line[0] != '#']
    return deps


description = ''  # type: str
long_description = ''  # type: str
if os.path.isfile(README_FILE):
    with io.open(README_FILE, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        long_description = f_in.read()
        description = long_description.splitlines()[3]

# use only if find_packages() doesn't work
# packages = [APP_NAME]  # type: List[str]

deps = get_deps_names(REQUIREMENTS_FILE)  # type: List[str]
deps_dev = get_deps_names(REQUIREMENTS_DEV_FILE)  # type: List[str]

# for windows creates a APP_NAME.exe, APP_NAME.py, APP_NAME_gui.exe and
# APP_NAME_gui.pyw under PYTHON_DIR/Scripts
# for other systems creates a APP_NAME.py and APP_NAME_gui.py under
# PYTHON_DIR/Scripts
# script_name = package.module:function
entry_points = {'console_scripts': [APP_NAME + '='
                                    + APP_NAME + '.'  # auto imported
                                    + APP_NAME + ':main'],
                # 'gui_scripts' : [APP_NAME + '_gui' + '='
                #                  + APP_NAME + '.'  # auto imported
                #                  + APP_NAME + ':main']
}  # type: Dict[str, List[str]]

package_data = {APP_NAME: ['*.rst'],}  # type: Dict[str, List[str]]

setup(name=APP_NAME,
      version=APP_VERSION,
      description=description,
      long_description=long_description,
      license=APP_LICENSE,
      url=APP_URL,
      author=APP_AUTHOR,
      author_email=APP_EMAIL,

      classifiers=CLASSIFIERS,
      keywords=APP_KEYWORDS,

      packages=find_packages(exclude=['contrib', 'doc', 'tests']),

      # use only if find_packages() doesn't work
      # packages=packages,
      # package_dir={'': APP_NAME},

      # Alternatively, if you want to distribute just a my_module.py, uncomment
      # this:
      # py_modules=['my_module'],

      # scripts=,  # don't use

      # To provide executable scripts, use entry points in preference to the
      # "scripts" keyword. Entry points provide cross-platform support and
      # allow pip to create the appropriate form of executable for the target
      # platform.
      entry_points=entry_points,

      # List run-time dependencies here.  These will be installed by pip when
      # your project is installed. For an analysis of "install_requires" vs
      # pip's requirements files see:
      # https://packaging.python.org/en/latest/requirements.html
      install_requires=deps,

      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[dev]
      extras_require={'dev': deps_dev},

      # used only if the package is not in PyPI, but exists as an
      # egg, sdist format or as a single .py file
      # see http://goo.gl/OgnjhO
      # dependency_links = ['http://host.domain.local/dir/'],

      # include_package_data=True,  # use MANIFEST.in during install

      # If there are data files included in your packages that need to be
      # installed, specify them here.  If using Python 2.6 or less, then these
      # have to be included in MANIFEST.in as well.
      # Relative to package path.
      package_data=package_data,

      # Although 'package_data' is the preferred approach, in some case you may
      # need to place data files outside of your packages. See:
      # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
      # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
      # Relative to package build path.
      # data_files=[('my_data', ['data/data_file'])],
      
      zip_safe=False
)
