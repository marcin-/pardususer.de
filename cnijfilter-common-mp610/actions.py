#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

WorkDir = "."

NoStrip = ["/"]

def install():

    pisitools.insinto("/usr/lib/cups/backend", "usr/lib/cups/backend/cnij_usb")
    pisitools.insinto("/usr/lib/cups/filter", "usr/lib/cups/filter/pstocanonij")

    pisitools.dobin("usr/local/bin/cngpij", "/usr/local/bin/")

    pisitools.dodoc("usr/share/doc/cnijfilter-common/LICENSE-cnijfilter-2.80E.txt")
    pisitools.dodoc("usr/share/doc/cnijfilter-common/LICENSE-cnijfilter-2.80J.txt")

