#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# Package Name : mbrola-voices-pl1
# Version : 1
# Summary : A polish female voice for mbrola.

WorkDir="."

def install():
    pisitools.dodoc("*.txt")
    shelltools.chmod("pl1", mode = 0644)
    pisitools.insinto("/usr/share/mbrola/pl1/", "pl1")
