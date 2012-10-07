#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():

# HACK: Remove fatal-warnings to succeed build with vala 0.13.
    shelltools.system("sed -i \"s:--fatal-warnings ::g\" Makefile plugins/Makefile.plugin.mk")

    autotools.configure("--prefix=/usr \
			 --disable-schemas-compile \
			 --disable-desktop-update \
			 --disable-icon-update")

def build(): 
    autotools.make() 

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "MAINTAINERS", "NEWS", "README", "THANKS")

