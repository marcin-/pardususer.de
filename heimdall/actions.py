#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools

WorkDir="Benjamin-Dobell-Heimdall-fbbed42/"

def setup():
    shelltools.cd("libpit")
    autotools.configure()
    shelltools.cd("../heimdall")
    autotools.configure()
    shelltools.cd("../heimdall-frontend")
    qt4.configure()

def build():
    shelltools.cd("libpit")
    autotools.make()
    shelltools.cd("../heimdall")
    autotools.make()
    shelltools.cd("../heimdall-frontend")
    qt4.make()

def install():
    shelltools.cd("heimdall")
    pisitools.dodoc("LICENSE", "description-pak", "doc-pak/LICENSE", "doc-pak/README")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../heimdall-frontend")
    qt4.install("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/local/bin/heimdall-frontend", "/usr/bin")
    pisitools.removeDir("/usr/local")
