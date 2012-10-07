#!/usr/bin/python
# -*- coding: iso-8859-9 -*-
#This is the illegal pardus version of the Cedega.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def install():
    pisitools.insinto("/", "usr")
    shelltools.copytree("usr/local/share/applications", "%s/usr/share" % get.installDIR())
    shelltools.copytree("usr/local/share/icons", "%s/usr/share" % get.installDIR())
    shelltools.copytree("usr/local/share/PeaZip", "%s/usr/share" % get.installDIR())
    pisitools.removeDir("/usr/local")
    pisitools.dosym("/usr/share/PeaZip/peazip", "/usr/bin/peazip")
    pisitools.dosym("/usr/share/PeaZip/res/pea", "/usr/bin/pea")
    pisitools.dosym("/usr/share/PeaZip/res/pealauncher", "/usr/bin/pealauncher")
    pisitools.removeDir("/usr/share/PeaZip/FreeDesktop_integration")
