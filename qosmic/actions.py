#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    qt4.configure(projectfile="qosmic.pro", parameters="CONFIG+=release CONFIG-=debug PREFIX=/usr")

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("changes.txt", "COPYING", "README", "README-LUA")