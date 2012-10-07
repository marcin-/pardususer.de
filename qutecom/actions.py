#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed('libs/pixertool/src/v4l/v4l-pixertool.c', 'linux/videodev.h', 'libv4l1-videodev.h')
    pisitools.dosed('libs/webcam/include/webcam/V4LWebcamDriver.h', 'linux/videodev.h', 'libv4l1-videodev.h')
    pisitools.dosed('libs/webcam/src/v4l/V4LWebcamDriver.cpp', '__u16', 'uint16_t')
    shelltools.makedirs('build')
    shelltools.cd('build')
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_SKIP_RPATH=OFF \
                          -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
                          -DCMAKE_INSTALL_RPATH=/usr/lib/qutecom \
                          -DLIBPURPLE_INTERNAL=OFF", installPrefix="/usr", sourceDir="..")

def build():
    shelltools.cd('build')
    cmaketools.make()

def install():
    pisitools.dodoc("README")
    shelltools.cd('build')
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("../../qutecom/AUTHORS", "/usr/share/doc/qutecom/AUTHORS")
    pisitools.dosym("../../qutecom/COPYING", "/usr/share/doc/qutecom/COPYING")

# By PiSiDo 2.0.0
