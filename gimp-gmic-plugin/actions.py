#!/usr/bin/python
# -*- actions.pycoding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#def setup():

def build():
    autotools.make("-C src all")

def install():
    autotools.rawInstall("-C src DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins/", "src/gmic_gimp")
    pisitools.dodoc("COPYING", "README")
    pisitools.insinto("/usr/share/doc/gimp-gmic-plugin", "COPYING")

# By PiSiDo 2.0.0
