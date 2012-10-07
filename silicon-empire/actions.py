#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="Silicon"

def build():
    autotools.make()

def install():
    shelltools.cd("build-linux/")
    pisitools.dobin("bin/silicon", "/usr/bin")
    shelltools.copytree("lib/", "%s/usr/lib/" % get.installDIR())
    shelltools.copytree("share/", "%s/usr/share/" % get.installDIR())
    
    shelltools.cd("../src/Files/")
    pisitools.insinto("/usr/share/applications", "silicon.desktop")
    shelltools.cd("icons/")
    pisitools.insinto("/usr/share/icons/hicolor/22x22/apps/", "silicon_22.png", "silicon.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps/", "silicon_32.png", "silicon.png")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/", "silicon_48.png", "silicon.png")
    pisitools.insinto("/usr/share/icons/hicolor/64x64/apps/", "silicon_64.png", "silicon.png")
    pisitools.insinto("/usr/share/icons/hicolor/128x128/apps/", "silicon_128.png", "silicon.png")

    shelltools.cd("../../../")  
    pisitools.dodoc("Authors", "COPYING", "COPYING.LESSER", "README")
