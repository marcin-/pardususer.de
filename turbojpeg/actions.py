#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
# See https://aur.archlinux.org/packages.php?ID=52359

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "--prefix=/usr \
               --without-jpeg8 \
               --mandir=/usr/share/man"
               
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        
    autotools.autoreconf("-fiv")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/include", "jpegint.h")
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share")
    pisitools.remove("/usr/include/j*.h")
    pisitools.remove("/usr/lib/libj*")
    pisitools.dodoc("ChangeLog.txt", "LGPL.txt", "LICENSE.txt", "README", "README-turbo.txt", "usage.txt", "wizard.txt")
    
#    if get.buildTYPE() == "emul32":
#        pisitools.removeDir("something")
#        return

# By PiSiDo 2.0.0
