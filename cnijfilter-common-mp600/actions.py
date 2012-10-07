#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

def install():

    pisitools.insinto("/usr/lib/cups/backend", "usr/lib/cups/backend/cnij_usb")
    pisitools.insinto("/usr/lib/cups/filter", "usr/lib/cups/filter/pstocanonij")

    pisitools.dobin("usr/local/bin/cngpij", "/usr/local/bin/")

    pisitools.dodoc("usr/share/doc/cnijfilter-common-2.70/LICENSE-cnijfilter-2.70E.txt")
    pisitools.dodoc("usr/share/doc/cnijfilter-common-2.70/LICENSE-cnijfilter-2.70J.txt")

