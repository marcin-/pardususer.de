#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

# Use this as variables:
# Package Name : rawtherapee
# Version : 3.0.0
# Summary : Free RAW converter and digital photo processing software

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

# if archive have project in a sub directory:
WorkDir="rawtherapee-"+ get.srcVERSION() +"~dfsg1.orig"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCREDITSDIR=/usr/share/doc/rawtherapee \
                          -DLICENCEDIR=/usr/share/doc/rawtherapee", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
