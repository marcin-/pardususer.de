#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("p7zip -d mplayer-skins-"+ get.srcVERSION() +".7z")

def install():
    pisitools.insinto("/usr/share/mplayer/skins/", "*")