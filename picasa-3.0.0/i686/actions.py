#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Please Google, forgive me for your rezipped files
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def install():
    pisitools.insinto("/opt/google/picasa/3.0", "uninstall")
    pisitools.insinto("/usr/bin", "download-picasa")
    pisitools.dosym("/opt/google/picasa/3.0/bin/picasa", "/usr/bin/picasa")
    pisitools.dosym("/opt/google/picasa/3.0/desktop/picasa.xpm", "/usr/share/pixmaps/picasa.xpm")
    pisitools.dosym("/opt/google/picasa/3.0/desktop/picasa-kdehal.desktop", "/usr/kde/4/share/kde4/services/ServiceMenus/picasa-kdehal.desktop")
    pisitools.dosym("/opt/google/picasa/3.0/lib/npPicasa3.so", "/usr/lib/nsbrowser/plugins/npPicasa3.so")
 
