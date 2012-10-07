#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "brother-mfc490cw"

def install():
    shelltools.copytree("usr/", "%s/usr" % get.installDIR())
