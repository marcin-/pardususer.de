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
    shelltools.copy("LightScribe%20Host%20Software%201.8.15.1%20Linux.rpm", "%s/LightScribe-Host-Software-1.8.15.1-Linux.rpm" % get.workDIR())
    shelltools.system("rpm2targz -v %s/LightScribe-Host-Software-1.8.15.1-Linux.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/LightScribe-Host-Software-1.8.15.1-Linux.tar.gz" %get.workDIR())
    
def install():
    pisitools.insinto("/etc/", "./etc/*")
    pisitools.insinto("/usr/", "./usr/*")

# By PiSiDo 2.0.0
