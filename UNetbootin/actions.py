#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def setup():
    shelltools.system("lupdate unetbootin.pro")
    shelltools.system("lrelease unetbootin.pro")
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dobin("unetbootin")
    pisitools.insinto("/usr/share/unetbootin/", "*.qm")
    pisitools.dodoc("README.TXT")
