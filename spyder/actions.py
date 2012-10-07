#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("spyderlib/spyder.py", "http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html" , "http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html")
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.insinto ("/usr/share/doc/spyder", "spyderlib/__init__.py",  destinationFile = 'LICENSE')

# By PiSiDo 2.0.0
