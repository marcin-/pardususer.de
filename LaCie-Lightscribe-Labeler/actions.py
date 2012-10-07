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
    shelltools.copy("LaCie%20LightScribe%20Labeler%201.0%20Linux.rpm", "%s/LaCie-LightScribe-Labeler-1.0-Linux.rpm" % get.workDIR())
    shelltools.system("rpm2targz -v %s/LaCie-LightScribe-Labeler-1.0-Linux.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/LaCie-LightScribe-Labeler-1.0-Linux.tar.gz" %get.workDIR())
    
def install():
    pisitools.insinto("/usr/", "./usr/*")

# By PiSiDo 2.0.0
