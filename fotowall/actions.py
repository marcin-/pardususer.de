#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake")

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    #pisitools.insinto("/usr/share/fotowall/example-layouts/", "example-layouts/*")

    #shelltools.system("lrelease-qt4 fotowall.pro")
    pisitools.insinto("/usr/share/fotowall/i18n/", "translations/*.qm")

    pisitools.dodoc("GPL_V2", "README*")
