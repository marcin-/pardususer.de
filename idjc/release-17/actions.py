#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #Remove internal libshout to be sure it's using system one
    shelltools.unlinkDir("libshout")

    # In order to avoid sandbox violations.
    shelltools.unlink("py-compile" )
    shelltools.sym("/bin/true", "py-compile")
    
    #Fix docdir
    pisitools.dosed("Makefile.in", "{PACKAGE_NAME}-\${PACKAGE_VERSION}", "{PACKAGE_NAME}")

    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")

# By PiSiDo 2.0.0
