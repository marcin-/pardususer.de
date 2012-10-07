#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools


WorkDir="."

def install():
    shelltools.system("wget http://winetricks.org/winetricks")
    shelltools.system("chmod 0777 winetricks")
    pisitools.insinto("/usr/share/winetrick/","winetricks")
    #shelltools.system("env WINEPREFIX=~/.wine winetricks mfc42")