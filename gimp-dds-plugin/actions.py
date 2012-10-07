#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.doexe("dds", "/usr/lib/gimp/2.0/plug-ins")

    pisitools.dodoc("doc/gimp-dds.pdf", "COPYING", "LICENSE", "README*", "TODO")

# By PiSiDo 2.0.0
