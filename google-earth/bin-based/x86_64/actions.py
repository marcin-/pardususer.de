#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/lib/googleearth", "uninstall")
    pisitools.insinto("/usr/bin", "download-googleearth")
    pisitools.dosym("/usr/lib32/libfontconfig.so.1.4.4","/usr/lib32/libfontconfig.so.1")
    pisitools.dosym("/usr/lib32/libfreetype.so.6.6.2","/usr/lib32/libfreetype.so.6")
    pisitools.dosym("/usr/lib32/libX11.so.6.3.0","/usr/lib32/libX11.so.6")
    pisitools.dosym("/usr/lib32/libXext.so.6.4.0","/usr/lib32/libXext.so.6")
    pisitools.dosym("/usr/lib32/libXrender.so.1.3.0","/usr/lib32/libXrender.so.1")
    pisitools.dosym("/usr/lib32/libGL.so.260.19.29","/usr/lib32/libGL.so.1")
    pisitools.dosym("/usr/lib32/libz.so.1.2.5","/usr/lib32/libz.so.1")
    pisitools.dosym("/usr/lib32/libSM.so.6.0.1","/usr/lib32/libSM.so.6")
    pisitools.dosym("/usr/lib32/libICE.so.6.3.0","/usr/lib32/libICE.so.6")
    pisitools.dosym("/usr/lib32/libexpat.so.1.5.2","/usr/lib32/libexpat.so.1")
    pisitools.dosym("/usr/lib32/libxcb.so.1.1.0","/usr/lib32/libxcb.so.1")
    pisitools.dosym("/usr/lib32/libXau.so.6.0.0","/usr/lib32/libXau.so.6")
    pisitools.dosym("/usr/lib32/libXdmcp.so.6.0.0","/usr/lib32/libXdmcp.so.6")
