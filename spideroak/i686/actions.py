#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
  
NoStrip = ["/"]         # stripping disabled
KeepSpecial=["python"]  # do not remove .pyc files

content_of_rpmunpack = "SpiderOak-9860-1.fc13.i386.rpm"

def setup():
    shelltools.system("rpm2targz SpiderOak-9860-1.fc13.i386.rpm")
    shelltools.system("tar -zxvf SpiderOak-9860-1.fc13.i386.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "etc")
