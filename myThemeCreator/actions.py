#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."


def setup():
    # Fix for the linux version of mTC: http://www.myforum.lasyk.net/showpost.php?p=413254&postcount=1586
    shelltools.cd("%s/" %get.workDIR())
    shelltools.move("./*.jar", "./lib/")
    shelltools.chmod("./lib/*.jar", 0755)
    shelltools.move("./lib/mTC.jar", ".")

def install():
    pisitools.insinto("/opt/myThemeCreator/", "bin/")
    pisitools.insinto("/opt/myThemeCreator/", "lib/")
    pisitools.insinto("/opt/myThemeCreator/", "mTC.jar")
    pisitools.dosym("/opt/myThemeCreator/myThemeCreator.sh", "/usr/bin/myThemeCreator")