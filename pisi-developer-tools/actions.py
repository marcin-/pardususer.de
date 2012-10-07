#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."


def setup():
    shelltools.chmod("*", 0755)
    shelltools.chmod("./template/*", 0755)
    shelltools.chmod("menu-icon-checksum.png", 0644)


def install():
    pisitools.insinto("/usr/share/pixmaps/", "menu-icon-checksum.png")

    pisitools.insinto("/usr/share/pisi-developer-tools/", "*")

    pisitools.dosym("/usr/share/pisi-developer-tools/pisi-developer-tools.sh", "/usr/bin/pisi-developer-tools")

    shelltools.cd(get.installDIR() + "/usr/share/pisi-developer-tools/")

    for file in shelltools.ls("*.desktop"):
        pisitools.dosym("/usr/share/pisi-developer-tools/"+file, "/usr/share/kde4/services/ServiceMenus/"+file)

    print "\n\n--=== Yeah! Go go go!!! ===--\n\nPardusUser.de 4 Ever!  :D\n\n"