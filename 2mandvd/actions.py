#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "2ManDVD"

def setup():
    qt4.configure()
    # fix path for chmod
    pisitools.dosed("Makefile", "(chmod\s-R\s\d+\s)(\/usr\/share\/2ManDVD)", r"\1$(INSTALL_ROOT)\2")

def build():
    qt4.make()

def install():
    qt4.install(parameters = 'INSTALL_ROOT=%s' % get.installDIR())
#    for it in ["Bibliotheque",  "Interface",   "2ManDVD",  "fake.pl",  "*.qm"]:
#        pisitools.insinto("/usr/share/2ManDVD", it)
#    pisitools.insinto("/usr/share/pixmaps", "Interface/mandvd.png", "2mandvd.png")
    pisitools.dodoc("copying",  "README.txt")
