#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def install():
    shelltools.system("zcat pl_basewords.dat.gz > pl_basewords.dat")
    pisitools.insinto("/usr/share/milena-words", "pl_basewords.dat")
# By PiSiDo 2.0.0
