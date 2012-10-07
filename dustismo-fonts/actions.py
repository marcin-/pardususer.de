#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

PkgSrcDir = "dustismo-fonts-" + get.srcVERSION();


def setup():
    shelltools.chmod("*",0644)

    shelltools.chmod("dustismo/*",0644)


def install():
    pisitools.insinto("/usr/share/fonts/", "*.ttf")

    pisitools.dodoc("COPYING", "INSTALL", "README")

    shelltools.cd(get.workDIR() +"/"+ PkgSrcDir +"/dustismo/")
    for file in shelltools.ls("*.ttf"):
        pisitools.insinto("/usr/share/fonts/dustismo/", file)