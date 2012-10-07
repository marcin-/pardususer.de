#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qiviewer"

def setup():
    shelltools.cd("src")
    qt4.configure(projectfile="qiviewer.pro", parameters="CONFIG+=release CONFIG-=debug CONFIG+=enable-webp PREFIX=/usr")

def build():
    shelltools.cd("src")
    qt4.make()

def install():
    shelltools.cd("src")
    qt4.install()
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")