#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("P7ZIP_SOURCE_DIR", "%s/p7zip_9.13" % get.workDIR())
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dolib_a("Lib7Zip/lib7zip.a")
    pisitools.insinto("/usr/include", "Lib7Zip/lib7zip.h")

# By PiSiDo 2.0.0
