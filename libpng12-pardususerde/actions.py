#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # we need remove some files for work right with libpng
    pisitools.removeDir("/usr/share/man")
    pisitools.remove("/usr/bin/libpng-config")
    pisitools.remove("/usr/include/*.h")

    if get.buildTYPE() == "emul32":
        pisitools.remove("/usr/lib32/libpng.la")
        pisitools.remove("/usr/lib32/libpng.so")
        pisitools.remove("/usr/lib32/pkgconfig/libpng.pc")

    else:
        pisitools.remove("/usr/lib/libpng.la")
        pisitools.remove("/usr/lib/libpng.so")
        pisitools.remove("/usr/lib/pkgconfig/libpng.pc")

    pisitools.dodoc("ANNOUNCE", "CHANGES", "KNOWNBUG", "README", "TODO")
