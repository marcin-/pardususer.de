#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    # remove la symlink
    pisitools.remove("/usr/lib/libpng.la")
    
    pisitools.remove("/usr/bin/libpng12-config")
    pisitools.remove("/usr/bin/libpng-config")
    pisitools.remove("/usr/include/pngconf.h")
    pisitools.remove("/usr/include/png.h")
    pisitools.remove("/usr/include/libpng12/pngconf.h")
    pisitools.remove("/usr/include/libpng12/png.h")
    pisitools.remove("/usr/lib/libpng.so")
    pisitools.remove("/usr/lib/libpng.so.3")
    pisitools.remove("/usr/lib/libpng.so.3.44.0")
    pisitools.remove("/usr/lib/pkgconfig/libpng12.pc")
    pisitools.remove("/usr/lib/pkgconfig/libpng.pc")
    pisitools.remove("/usr/share/man/man3/libpng.3")
    pisitools.remove("/usr/share/man/man3/libpngpf.3")
    pisitools.remove("/usr/share/man/man5/png.5")
