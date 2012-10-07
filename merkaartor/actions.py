#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="merkaartor-%s" % (get.srcVERSION())


def setup():
    qt4.configure(projectfile="Merkaartor.pro", parameters="NODEBUG=1 GEOIMAGE=1 LIBPROXY=1 GPSDLIB=1 PREFIX=/usr")

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("CREDITS", "LICENSE", "AUTHORS", "HACKING", "INSTALL", "CHANGELOG", "TODO", "LICENSE.rtf")