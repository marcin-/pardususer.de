#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "%s-%shg" % (get.srcNAME(),  get.srcVERSION())
shelltools.export("CCACHE_DIR",  get.workDIR())

def setup():
    qt4.configure()
    
def build():
    qt4.make()
    
def install():
    qt4.install()
    pisitools.dodoc("COPYING", "README")
    shelltools.chmod(get.installDIR() + "/usr/lib/gimp/2.0/plug-ins/ptGimp", 0755)
