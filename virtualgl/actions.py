#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
# See https://aur.archlinux.org/packages.php?ID=52360 and http://aur.archlinux.org/packages.php?ID=52473

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "-DCMAKE_BUILD_TYPE=release \
               -DCMAKE_INSTALL_PREFIX=/opt/VirtualGL \
               -DTJPEG_INCLUDE_DIR=/usr/include \
               -DTJPEG_LIBRARY=/usr/lib/libturbojpeg.so \
               -DVGL_LIBDIR=/usr/lib \
               -DVGL_BINDIR=/usr/bin"
               
    if get.buildTYPE() == "emul32":
        options += " -DTJPEG_LIBRARY=/usr/lib32/libturbojpeg.so \
                     -DVGL_LIBDIR=/usr/lib32 \
                     -DX11_X11_LIB=/usr/lib32/libX11.so \
                     -DX11_Xext_LIB=/usr/lib32/libXext.so \
                     -DOPENGL_gl_LIBRARY=/usr/lib32/libGL.so"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CC())
              
    cmaketools.configure(options, installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#    if get.buildTYPE() == "emul32":
#        pisitools.removeDir("something")

    pisitools.dosym("/usr/bin/glxinfo", "/opt/VirtualGL/bin/glxinfo")

# By PiSiDo 2.0.0
