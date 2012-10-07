#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("share/sinthgunt.desktop", "(GenericName)(=Video converter)", r"\1\2\n\1[pl]=Video konwerter")
    pisitools.dosed("share/sinthgunt.desktop", "(Comment)(=Convert video files)", r"\1\2\n\1[pl]=Konwertuje pliki video")
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.domove("/usr/share/sinthgunt/*.txt", "/usr/share/doc/sinthgunt/")
