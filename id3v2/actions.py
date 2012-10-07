#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

#WorkDir="id3v2-"+get.srcVERSION()


def build():
    #pisitools.remove("id3v2")
    #pisitools.remove("id3v2.1")
    autotools.make()


def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("id3v2")
    pisitools.dobin("id3v2.1")
    #pisitools.doman("id3v2")
    #pisitools.docdoc("COPYING","README")