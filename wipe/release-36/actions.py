#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


WorkDir = "wipe-" + get.srcVERSION()
 

def setup():
    autotools.configure("--prefix=usr")



def install():
    autotools.install()
    pisitools.dodoc("CHANGES","INSTALL","LICENSE","README","TESTING","TODO","copyright")