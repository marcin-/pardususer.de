#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

shelltools.export("XDG_CACHE_HOME",  get.workDIR())
shelltools.export("XDG_DATA_HOME",  get.workDIR())
shelltools.export("GIMP2_DIRECTORY",  get.workDIR())

#def setup():

def build():
    autotools.make("-j2")

def install():
    autotools.rawInstall("INSTALL_DIR=%s/usr/share/openttd/data/opengfx" % get.installDIR())
    pisitools.dodir("/usr/share/doc/openttd-opengfx")
    shelltools.cd("opengfx-%s" % get.srcVERSION())
    for it in shelltools.ls("*.txt"):
        pisitools.dosym("/usr/share/openttd/data/opengfx/%s" % it,  "/usr/share/doc/openttd-opengfx/%s" % it)
