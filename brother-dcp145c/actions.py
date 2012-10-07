#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "brother-dcp145c"

def install():
    shelltools.copytree("usr/", "%s/usr" % get.installDIR())
