#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def build():
    shelltools.system("make -f makefile.linux")

def install():
    pisitools.dobin("out/makemkv")
    pisitools.insinto("/usr/lib/","out/libdriveio.so.0")
    pisitools.insinto("/usr/lib/","out/libmakemkv.so.1")
