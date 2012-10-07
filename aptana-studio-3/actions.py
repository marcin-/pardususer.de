#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "Aptana_Studio_3"
NoStrip = ["/"]
shelltools.export("HOME", get.workDIR())

def install():
    shelltools.chmod(get.workDIR() +"/"+ WorkDir +"/studio3")
    pisitools.insinto("/opt/AptanaStudio3/", "*")
    pisitools.dosym("/opt/AptanaStudio3/studio3", "/usr/bin/AptanaStudio3")