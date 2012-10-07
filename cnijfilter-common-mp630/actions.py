#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

NoStrip = ["/"]

def setup():
    for d in ("libs", "cngpij"):
        shelltools.cd(d)
        autotools.configure()
        shelltools.cd("..")

    pisitools.dosed("filter/Makefile", "\.\./\.\./libs", "../libs")

def build():
    for d in ("libs", "filter", "cngpij", "."):
        autotools.make("-C %s" % d)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/cups/filter", "filter/pstocanonij")
    pisitools.dobin("cngpij/cngpij/cngpij", "/usr/local/bin/")

    pisitools.dodoc("LICENSE*")
