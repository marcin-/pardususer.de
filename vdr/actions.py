#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())
    autotools.make()
    autotools.make("all plugins")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.insinto("/video", "*.conf*")
    pisitools.dodoc("CONTRIBUTORS", "COPYING", "PLUGINS.*", "README*")

