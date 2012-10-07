#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

# Use this as variables:
# Package Name : posterazor
# Version : 1.9.6
# Summary : Print Your own poster at home

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools


# if archive have project in a sub directory:
WorkDir="posterazor/src/"


def setup():
    shelltools.system("qmake posterazor.pro")


def build():
    qt4.make()

def install():
     pisitools.insinto("/usr/bin/","PosteRazor")


#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
#    pisitools.dobin("posterazor")
