#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
NoStrip = ["/"]

def setup():
    shelltools.system("rpm2targz -v %s/google-chrome-stable_current_i386.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/google-chrome-stable_current_i386.tar.gz --exclude=usr/share/gnome-control-center --exclude=usr/bin --exclude=etc" %get.workDIR())
    shelltools.chmod("%s/opt/google/chrome/*" %get.workDIR())

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/usr/", "./usr/*")
    shelltools.system("chmod -v 4755 %s/opt/google/chrome/chrome-sandbox" %get.installDIR())
    pisitools.dosym("/opt/google/chrome/google-chrome", "/usr/bin/google-chrome")
    pisitools.dosym("/opt/google/chrome/google-chrome.desktop", "/usr/share/applications/google-chrome.desktop")
    pisitools.dosym("/opt/google/chrome/product_logo_32.xpm", "/usr/share/pixmaps/google-chrome.xpm")
    pisitools.dosym("/opt/google/chrome/product_logo_256.png", "/usr/share/pixmaps/google-chrome.png")
    pisitools.dosym("/usr/lib/nss/libnss3.so", "/usr/lib/libnss3.so.1d")
    pisitools.dosym("/usr/lib/nss/libnssutil3.so", "/usr/lib/libnssutil3.so.1d")
    pisitools.dosym("/usr/lib/nss/libsmime3.so", "/usr/lib/libsmime3.so.1d")
    pisitools.dosym("/usr/lib/libplc4.so", "/usr/lib/libplc4.so.0d")
    pisitools.dosym("/usr/lib/libnspr4.so", "/usr/lib/libnspr4.so.0d")
    pisitools.dosym("/lib/libbz2.so", "/usr/lib/libbz2.so.1.0")