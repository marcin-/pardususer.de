#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

# Package Name : mbrola
# Version : 1
# Summary : A polish female voice for mbrola.

WorkDir="."

def install():
    pisitools.dodoc("*.txt")
    pisitools.dobin("mbrola-linux-i386")
    pisitools.dosym("/usr/bin/mbrola-linux-i386", "/usr/bin/mbrola")
