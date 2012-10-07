#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

#def setup()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("changelog.txt", "COPYING")
