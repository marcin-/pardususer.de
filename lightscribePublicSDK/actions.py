#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/"]

def setup():
    shelltools.system("rpm2targz -v %s/lightscribePublicSDK-1.18.6.1-linux-2.6-intel.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/lightscribePublicSDK-1.18.6.1-linux-2.6-intel.tar.gz" %get.workDIR())
    
def install():
    pisitools.insinto("/usr/", "./usr/*")

# By PiSiDo 2.0.0
