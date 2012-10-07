#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="./RealtimeSync/"


def build():
    pisitools.dosed("Makefile", "-lboost_thread", "-lboost_thread-mt")
    autotools.make()



def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#    pisitools.dodoc("*.txt")

#    shelltools.chmod("%s/usr/share/FreeFileSync/*" % get.installDIR(), mode = 0644)
#    shelltools.chmod("%s/usr/share/FreeFileSync/Languages/*" % get.installDIR(), mode = 0644)
#    shelltools.chmod("%s/usr/share/FreeFileSync/Help/*" % get.installDIR(), mode = 0644)
#    shelltools.chmod("%s/usr/share/FreeFileSync/Help/html/*" % get.installDIR(), mode = 0644)
    
    
