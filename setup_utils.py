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

"""Setup utils library."""

import datetime as dt
import glob
import io
import os
# import pprint as pp
import sys
# import sysconfig
import time
from typing import List, Optional, Tuple
import zipfile as zipf

from appinfo import (APP_AUTHOR, APP_EMAIL, APP_KEYWORDS, APP_LICENSE,
                     APP_NAME, APP_URL, APP_VERSION, CLASSIFIERS, COPYRIGHT,
                     README_FILE, REQUIREMENTS_FILE, REQUIREMENTS_DEV_FILE)


UTF = 'utf-8'  # type: str
UNTOUCHABLES = ('appinfo.py', 'build.cmd', 'setup_utils.py')  # type: Tuple[str]


def read_text(filename: str) -> Optional[List[str]]:
    """Read text from filename.
    
    :param filename: filename to read.
    :return: text from filename or None.
    """
    assert isinstance(filename, str)
    with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        return f_in.readlines()  # type: Optional[List[str]]


def is_copyright_updated(text: str) -> bool:
    """Check if copyright is updated.
    
    :param text: text to check.
    :return: True if copyright is updated.
    """
    assert isinstance(text, str)
    update_required = False  # type: bool
    for line in text:  # type: str
        if COPYRIGHT in line:
            break
        elif 'Copyright 2009-' in line:
            print('Copyright in ' + filename + ' is not updated.')
            update_required = True
            break
    return update_required


def check_copyright() -> Optional[int]:
    """Check copyright on files that have to be updated manually.
    
    :returns: None if no update needed or 1 otherwise.
    """
    update_required = False  # type: bool
    for filename in UNTOUCHABLES:  # type: str
        if os.path.isfile(filename):
            text = read_text(filename)  # type: Optional[List[str]]
            update_required = any(update_required, is_copyright_updated(text))
    if update_required:
        sys.exit(1)


def update_copyright() -> None:
    """Update copyright on source and license files."""
    filenames = glob.glob('*.py')  # type: Optional[List[str]]
    filenames = [filename for filename in filenames
                 if filename not in UNTOUCHABLES]
    filenames += glob.glob(APP_NAME + '/*.py')
    for filename in filenames:  # type: str
        with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            text = f_in.readlines()  # type: Optional[List[str]]
        new_text = ''  # type: str
        changed = False  # type: bool
        for line in text:  # type: str
            if all([not changed, COPYRIGHT not in line,
                    '# Copyright 2009-' in line]):
                new_text += '# ' + COPYRIGHT + '\n'
                changed = True
            else:
                new_text += line
        if changed:
            with io.open(filename, 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
                f_out.writelines(new_text)

    filename = 'doc/conf.py'  # type: str
    if os.path.isfile(filename):
        with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            text = f_in.readlines()
        new_text = ''
        changed = False
        doc_copyright = ("copyright = u'2009-" + str(dt.date.today().year)
                         + ', ' + APP_AUTHOR + "'")  # type: str
        for line in text:  # type: str
            if all([not changed, "copyright = u'2009-" in line,
                    doc_copyright not in line]):
                new_text += doc_copyright + '\n'
                changed = True
            else:
                new_text += line
        if changed:
            with io.open(filename, 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
                f_out.writelines(new_text)

    filename = 'LICENSE.rst'
    with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()
    new_text = ''
    changed = False
    for line in text:  # type: str
        if all([not changed, COPYRIGHT not in line,
                'Copyright 2009-' in line]):
            new_text += '        ' + COPYRIGHT + '\n'
            changed = True
        else:
            new_text += line
    if changed:
        with io.open(filename, 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
            f_out.writelines(new_text)


def sleep(seconds: float = 5.0) -> None:
    """Pause for specified time.

    :param seconds: number of seconds to sleep.
    """
    assert isinstance(seconds, float)
    time.sleep(seconds)


def app_name() -> None:
    """Write application name to text file."""
    with io.open('app_name.txt', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.write(APP_NAME)


def app_ver() -> None:
    """Write application version to text file if equal to CHANGES.rst."""
    with io.open('CHANGES.rst', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        change_app_ver = f_in.readline().split()[0]  # type: str
    if change_app_ver == APP_VERSION:
        with io.open('app_ver.txt', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
            f_out.write(APP_VERSION)
    else:
        print('Version in CHANGES.rst and __init__.py are not in sync.')


def py_ver() -> None:
    """Write Python version to text file."""
    with io.open('py_ver.txt', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.write(str(sys.version_info.major) + '.'
                    + str(sys.version_info.minor))


def remove_copyright() -> None:
    """Remove Copyright from README.rst."""
    with io.open('README.rst', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()  # type: Optional[List[str]]

    new_text = ''  # type: str
    for line in text:  # type: str
        if 'Copyright ' in line:
            pass
        else:
            new_text += line

    with io.open('README.rst', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.writelines(new_text)


def prep_rst2pdf() -> None:
    """Remove parts of rST to create a better pdf."""
    with io.open('index.ori', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()  # type: Optional[List[str]]

    new_text = ''  # type: str
    for line in text:  # type: str
        if 'Indices and tables' in line:
            break
        else:
            new_text += line

    with io.open('index.rst', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.writelines(new_text)

    with io.open('../README.rst', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()

    new_text = ''
    for line in text:  # type: str
        if '.. image:: ' in line or '    :target: ' in line:
            pass
        else:
            new_text += line

    with io.open('../README.rst', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.writelines(new_text)


def create_doc_zip() -> None:
    """Create doc.zip to publish in PyPI."""
    doc_path = APP_NAME + '/doc'  # type: str
    with zipf.ZipFile('pythonhosted.org/doc.zip', 'w') as archive:  # type: zipfile.ZipFile
        for root, _, filenames in os.walk(doc_path):  # type: str, List[str], List[str]
            for filename in filenames:  # type: str
                if '.pdf' not in filename:
                    pathname = os.path.join(root, filename)  # type: str
                    sub_pathname = pathname.replace(doc_path + os.sep,
                                                    '')  # type: str
                    archive.write(pathname, sub_pathname)


def upd_usage_in_readme() -> None:
    """Update usage in README.rst."""
    if os.path.isfile(APP_NAME + '/usage.txt'):
        with io.open(APP_NAME + '/usage.txt', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            usage_text = f_in.read()  # type: str
            usage_text = usage_text[len(os.linesep) - 1:]  # remove 1st line

        with io.open('README.rst', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            text = f_in.readlines()  # type: Optional[List[str]]

        new_text = ''  # type: str
        usage_section = False  # type: bool
        changed = False  # type: bool
        for line in text:  # type: str
            if 'usage: ' in line:  # usage section start
                usage_section = True
                new_text += usage_text + '\n'
                changed = True
            elif usage_section and 'Resources' not in line:
                # bypass old usage section
                continue
            elif usage_section and 'Resources' in line:  # usage section end
                usage_section = False
                new_text += line
            else:
                new_text += line

        if changed:
            with io.open('README.rst', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
                f_out.writelines(new_text)


def change_sphinx_theme() -> None:
    """"Change Sphinx theme according to Sphinx version."""
    try:
        import sphinx
        sphinx_ver_str = sphinx.__version__  # type: str
        sphinx_ver = int(sphinx_ver_str.replace('.', ''))

        with io.open('doc/conf.py', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            text = f_in.readlines()  # type: Optional[List[str]]

        new_text = ''  # type: str
        changed = False  # type: bool
        for line in text:  # type: str
            if "html_theme = 'default'" in line and sphinx_ver >= 131:
                new_text += "html_theme = 'alabaster'\n"
                changed = True
            elif "html_theme = 'alabaster'" in line and sphinx_ver < 131:
                new_text += "html_theme = 'default'\n"
                changed = True
            else:
                new_text += line

        if changed:
            with io.open('doc/conf.py', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
                f_out.write(new_text)
    except ImportError:  # as error:
        pass


def comment_import_for_py2exe(filename: str) -> None:
    """Comment unicode_literals import in filename for py2exe build.
    
    :param filename: filename.
    """
    with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()  # type: Optional[List[str]]

    new_text = ''  # type: str
    for line in text:  # type: str
        if '                        unicode_literals)' in line:
            new_text += '                        )  # unicode_literals)\n'
        else:
            new_text += line

    with io.open(filename, 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.writelines(new_text)


def uncomment_import_for_py2exe(filename: str) -> None:
    """Uncomment unicode_literals import in filename for other builds.
        
    :param filename: filename.
    """
    with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()  # type: Optional[List[str]]

    new_text = ''  # type: str
    for line in text:  # type: str
        if '                        )  # unicode_literals)' in line:
            new_text += '                        unicode_literals)\n'
        else:
            new_text += line

    with io.open(filename, 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
        f_out.writelines(new_text)


def collect_to_do() -> None:
    """Collect To do from all py files."""
    files = glob.glob(APP_NAME + '/*.py')  # type: Optional[List[str]]
    to_do_lst = []  # type: List[str]
    for filename in files:  # type: str
        with io.open(filename, encoding=UTF) as f_in:  # type: _ioTextIOWrapper
            text = f_in.readlines()  # type: Optional[List[str]]
        for line in text:  # type: str
            if '# ToDo: ' in line:
                to_do_lst.append('* ' + filename.split(os.sep)[-1] + ': '
                                 + line.replace('# ToDo: ', '').lstrip())

    to_do_text = ''  # type: str
    for item in to_do_lst:  # type: str
        to_do_text += item

    with io.open('README.rst', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
        text = f_in.readlines()

    new_text = ''  # type: str
    to_do_section = False  # type: bool
    changed = False  # type: bool
    for line in text:  # type: str
        if '**To do**' in line:  # to do section start
            to_do_section = True
            new_text += '**To do**\n\n' + to_do_text + '\n'
            changed = True
        elif to_do_section and 'Installation' not in line:
            # bypass old to do section
            continue
        elif to_do_section and 'Installation' in line:  # to do section end
            to_do_section = False
            new_text += line
        else:
            new_text += line

    if changed:
        with io.open('README.rst', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
            f_out.writelines(new_text)


# def std_lib_modules() -> None:
#     """List all (not complete) Standard library modules."""
#     std_lib_dir = sysconfig.get_config_vars('LIBDEST')[0]  # type: str
#     modules_lst = []  # type: List[str]
#     for top, dirs, files in os.walk(std_lib_dir):  # type: str, List[str], List[str]
#         for nm in files:  # type: str
#             if nm != '__init__.py' and nm[-3:] == '.py':
#                 module = os.path.join(top, nm)[len(std_lib_dir)+1:-3].replace('\\','.')  # type: str
#                 if 'site-packages.' not in module:
#                     modules_lst.append(os.path.join(top, nm)[len(std_lib_dir)+1:-3].replace('\\','.'))
#     pp.pprint(modules_lst)


# def non_std_lib_modules() -> None:
#     """List all non Standard library modules."""
#     site_lib_dir = sysconfig.get_config_vars('LIBDEST')[0]  # type: str
#     site_lib_dir += '/site-packages'
#     modules_lst = []  # type: List[str]
#     for top, dirs, files in os.walk(site_lib_dir):  # type: str, List[str], List[str]
#         for nm in files:  # type: str
#             if nm != '__init__.py' and nm[-3:] == '.py':
#                 modules_lst.append(os.path.join(top, nm)[len(site_lib_dir)+1:-3].replace('\\','.'))
#     pp.pprint(modules_lst)


# def docstr2readme() -> None:
#     """Copy main module docstring to README.rst."""
#     with io.open(APP_NAME + '/' + APP_NAME + '.py',
#                  encoding=UTF) as f_in:  # type: _ioTextIOWrapper
#         text = f_in.readlines()  # type: Optional[List[str]]
#
#     text2copy = APP_NAME + '\n' + '=' * len(APP_NAME) + '\n\n'  # type: str
#
#     start_copy = False  # type: bool
#     for line in text:  # type: str
#         if '"""' in line:
#             if start_copy:
#                 break
#             else:
#                 start_copy = True
#         elif start_copy:
#             text2copy += line
#
#     text2copy += '\n'
#
#     with io.open('README.rst', encoding=UTF) as f_in:  # type: _ioTextIOWrapper
#         text = f_in.readlines()
#
#     until_eof = False  # type: bool
#
#     for line in text:  # type: str
#         if 'Resources' in line or until_eof:
#             text2copy += line
#             until_eof = True
#
#     with io.open('README.rst', 'w', encoding=UTF) as f_out:  # type: _ioTextIOWrapper
#         f_out.writelines(text2copy)


if __name__ == '__main__':
    eval(sys.argv[1])
