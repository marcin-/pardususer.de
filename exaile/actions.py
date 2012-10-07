#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def build():
    autotools.make()

def install():

    autotools.rawInstall("DESTDIR=/%s PREFIX=/%s \
                        XDG_DATA_DIRS=/usr/share \
                        XDG_CONFIG_DIRS=/etc/xdg \
                        LIBINSTALLDIR=/usr/lib/%s/site-packages" % (get.installDIR(),get.defaultprefixDIR(),get.curPYTHON()))

    pisitools.dodoc("FUTURE","README","COPYING")

