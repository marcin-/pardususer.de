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
    shelltools.system("rpm2targz -v %s/lightscribe-1.18.24.1-linux-2.6-intel.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/lightscribe-1.18.24.1-linux-2.6-intel.tar.gz" %get.workDIR())
    pisitools.dosed("etc/lightscribe.rc", "UpdateScriptDir=/usr/lib/lightscribe/update;", "UpdateScriptDir=/usr/lib/lightscribe/updates;")
    
    
def install():
    pisitools.insinto("/etc/", "./etc/*")
    pisitools.insinto("/usr/", "./usr/*")

# By PiSiDo 2.0.0
