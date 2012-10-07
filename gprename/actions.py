#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "%s/trunk" % get.srcNAME()

def setup():
    pisitools.dosed("bin/gprename", "courier new", "DejaVu Sans Mono")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s/usr" % get.installDIR())
    pisitools.dodoc("COPYING", "README")
