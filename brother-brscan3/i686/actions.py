#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():

    shelltools.copytree("usr", "%s/usr" % get.installDIR())
