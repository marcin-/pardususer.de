#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = get.srcNAME()
arch = ""
if get.ARCH() == "x86_64": arch = "64"

#def setup():
    
def build():
    autotools.make("libfacebook%s.so" % arch)
    
def install():
    pisitools.insinto("/usr/lib/purple-2", "libfacebook%s.so" % arch)
    for it in [16,  22,  48]: pisitools.insinto("/usr/share/pixmaps/pidgin/protocols/%s" % it,  "facebook%s.png" % it)
    pisitools.dodoc("COPYING")
