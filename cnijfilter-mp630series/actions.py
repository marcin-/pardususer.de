#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

NoStrip = ["/"]

def install():
    pisitools.copytree("usr", "%s/usr" % get.installDIR())

    for lib in shelltools.ls("%s/usr/lib/*.so*" % get.installDIR()):
        pisitools.dosym(os.path.basename(lib), "/usr/lib/%s.so" % os.path.basename(lib).split(".")[0])
