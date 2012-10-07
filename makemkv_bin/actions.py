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
    if get.ARCH() == "x86_64": pisitools.dobin("bin/amd64/makemkvcon")
    else: pisitools.dobin("bin/i386/makemkvcon")

    pisitools.dodoc("src/eula_en_linux.txt")
