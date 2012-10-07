#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("AUTHORS", "TRANSLATORS", "CHANGELOG", "COPYING", "README")
