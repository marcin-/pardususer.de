#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools

WorkDir = get.srcNAME()

def setup():
    pisitools.dosed("starter/qt4-fsarchiver.desktop", "sudo", "xdg-su -c")
    pisitools.dosed("starter/qt4-fsarchiver.desktop", "^(Terminal=).*", r"\1false")
    pisitools.dosed("starter/qt4-fsarchiver.desktop", "app-install/icons/harddrive.png", "pixmaps/qt4-fsarchiver.png")
    pisitools.dosed("qt4-fsarchiver.pro", "(icon.path\s=\s\/usr\/share\/).*", r"\1/pixmaps")
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("copyright", "Change",  "Readme")
    pisitools.domove("/usr/share/pixmaps/harddrive.png", "/usr/share/pixmaps",  "qt4-fsarchiver.png")
