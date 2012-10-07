#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ntadej-tano-78a3b67"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
			  -DCMAKE_BUILD_TYPE=Release \
			  -DCMAKE_CXX_FLAGS_RELEASE:STRING='-DNDEBUG' \
			  -DCMAKE_C_FLAGS_RELEASE:STRING='-DNDEBUG' \
                          -DEDITOR_WITH_VLCQT=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "INSTALL", "NEWS", "LICENSE.GPL", "README", "VERSION")
