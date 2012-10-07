#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Synkron-%s-src" % get.srcVERSION()

def setup():
    shelltools.system("lrelease Synkron.pro")
    shelltools.system("qmake -config release")

def build():
    autotools.make()

def install():
    pisitools.dobin("synkron")

    for i in("16", "48", "128"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i, i), "images/Synkron%s.png" %i, "synkron.png")

    pisitools.dodoc("*.txt")
