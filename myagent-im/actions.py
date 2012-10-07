#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import qt4
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = get.srcNAME()

def setup():
    qt4.configure()
    
def build():
    qt4.make()
    
def install():
    qt4.install()
    pisitools.dodoc("COPYING", "README.RU.UTF8.txt")
