#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system("iconv -f cp1251 -t utf8 rc/qmetro.desktop -o rc/qmetro.desktop")
    qt4.configure(projectfile="qmetro.pro", parameters="CONFIG+=release CONFIG-=debug PREFIX=/usr")

def build():
    qt4.make()

def install():
    qt4.install()
    shelltools.chmod("%s/usr/share/icons/hicolor/64x64/apps/qmetro.png" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/icons/hicolor/scalable/apps/qmetro.svg" % get.installDIR(), 0644)
    pisitools.dodoc("AUTHORS", "LICENSE", "README")