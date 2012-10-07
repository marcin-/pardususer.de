#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

# Use this as variables:
# Package Name : love
# Version : 0.7.2
# Summary : 2D game development framework based on Lua and OpenGL

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."

#def setup():
    
#def build():

def install():
    pisitools.insinto("/usr/share/games/nottetris2/", "Not Tetris 2.love", "nottetris2.love")
    pisitools.insinto("/usr/share/games/nottetris2/", "Not Readme.txt", "readme.txt")
    shelltools.chmod(get.installDIR() + "/usr/share/games/nottetris2/*", 0644)
    
