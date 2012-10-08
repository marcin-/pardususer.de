#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."

def build():
    shelltools.cd("libtommath-0.42.0")
    autotools.make()
    shelltools.cd("../lib")
    autotools.make()
    shelltools.cd("../clit18")
    shelltools.system("sed -i 's|libtommath-0.30|libtommath-0.42.0|' Makefile")
    autotools.make()

def install():
    pisitools.insinto("/usr/bin", "clit18/clit")
    pisitools.dodoc("README")