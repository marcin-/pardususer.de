#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("rpm2targz -v %s/picasa-3.0-current.i386.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/picasa-3.0-current.i386.tar.gz --exclude=usr --exclude=opt/kde3" %get.workDIR())

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.dosym("/opt/google/picasa/3.0/bin/picasa", "/usr/bin/picasa")
    pisitools.dosym("/opt/google/picasa/3.0/lib/npPicasa3.so", "/usr/lib/browser-plugins/npPicasa3.so")
    pisitools.dosym("/opt/google/picasa/3.0/desktop/picasa-kdehal.desktop", "/usr/share/kde4/services/ServiceMenus/picasa-kdehal.desktop")