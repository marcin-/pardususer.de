#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = ["/"]

def setup():
    shelltools.system("rpm2targz %s/ICAClient_12.1.0-0.x86_64.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/ICAClient_12.1.0-0.x86_64.tar.gz" %get.workDIR())

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.dosym("/opt/Citrix/ICAClient/desktop/wfcmgr.desktop", "/usr/share/applications/wfcmgr.desktop")
    pisitools.dosym("/opt/Citrix/ICAClient/nls/en/appsrv.ini", "/opt/Citrix/ICAClient/config/appsrv.ini")
    pisitools.dosym("/opt/Citrix/ICAClient/nls/en/module.ini", "/opt/Citrix/ICAClient/config/module.ini")
    pisitools.dosym("/opt/Citrix/ICAClient/nls/en/wfclient.ini", "/opt/Citrix/ICAClient/config/wfclient.ini")

# By PiSiDo 2.0.0
