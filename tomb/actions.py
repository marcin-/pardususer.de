#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


WorkDir = "Tomb-" + get.srcVERSION()

def setup():
    shelltools.system("autoreconf -i")
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR="+get.installDIR())
    #pisitools.dodoc("CHANGES","INSTALL","LICENSE","README","TESTING","TODO","copyright")
