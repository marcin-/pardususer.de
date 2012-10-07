#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "elbersb-otr-verwaltung-3a55130"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("AUTHORS","CHANGELOG","COPYING")