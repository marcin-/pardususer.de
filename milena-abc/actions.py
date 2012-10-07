#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()
    pisitools.dosed("Makefile", "/share/icons", "/share/pixmaps")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
