#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
# See http://aur.archlinux.org/packages.php?ID=51633

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

NoStrip = ["/"]

def setup():
    shelltools.system("ar x %s/VirtualGL32_2.3_amd64.deb" %get.workDIR())
    shelltools.system("tar xfvz %s/data.tar.gz --exclude=usr/bin --exclude=etc" %get.workDIR())

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/usr/", "./usr/*")

# By PiSiDo 2.0.0
