#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    qt4.configure(projectfile = 'ugene.pro', parameters = 'CONFIG+=x64 -r' if get.ARCH() == "x86_64" else '-r', installPrefix = '/usr')
    
def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("COPYRIGHT", "LICENSE", "data/license")
