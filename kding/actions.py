#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    cmaketools.configure(installPrefix="/usr", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.dosym("/usr/share/applications/kde4/kding.desktop","/usr/share/applications/kding.desktop")
    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/kding.png","/usr/share/pixmaps/kding.png")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")

