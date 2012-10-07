#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."


def setup():
    shelltools.cd("%s/" %get.workDIR())
    shelltools.system("unzip -j jai-1_1_3-lib.zip")
    shelltools.unlink("*.exe")
    shelltools.system("echo %s > PisiPackageRelease" %get.srcRELEASE())
    shelltools.chmod("*", 0755)
    shelltools.chmod("./mapsources/*", 0755)

def install():
    shelltools.unlink("pisiBuildState")
    pisitools.insinto("/opt/MobileAtlasCreator/","*")
    pisitools.dosym("/opt/MobileAtlasCreator/MobileAtlasCreator.sh", "/usr/bin/MobileAtlasCreator")
    pisitools.dodoc("*.txt","*.HTM")