#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="systeminfo-"+get.srcVERSION()

def install():
    pisitools.dobin("systeminfo-"+get.srcVERSION()+".sh")
    pisitools.dosym("/usr/bin/systeminfo-"+get.srcVERSION()+".sh","/usr/bin/systeminfo")
    pisitools.dodoc("AUTHORS", "COPYING","README")
    pisitools.insinto("/usr/share/pixmaps/", "systeminfo.png")
    pisitools.insinto("/usr/share/applications/", "systeminfo.desktop")