#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.insinto("/opt/qnext", "uninstall")
    pisitools.insinto("/usr/bin", "download-qnext")
    pisitools.dosym("/usr/lib32/libX11.so.6.3.0","/usr/lib32/libX11.so.6")
    pisitools.dosym("/usr/lib32/libXau.so.6.0.0","/usr/lib32/libXau.so.6")
    pisitools.dosym("/usr/lib32/libxcb.so.1.1.0","/usr/lib32/libxcb.so.1")
    pisitools.dosym("/usr/lib32/libXdmcp.so.6.0.0","/usr/lib32/libXdmcp.so.6")
    pisitools.dosym("/usr/lib32/libXext.so.6.4.0","/usr/lib32/libXext.so.6")
    pisitools.dosym("/usr/lib32/libXi.so.6.1.0","/usr/lib32/libXi.so")
    pisitools.dosym("/usr/lib32/libXi.so.6.1.0","/usr/lib32/libXi.so.6")
    pisitools.dosym("/usr/lib32/libXtst.so.6.1.0","/usr/lib32/libXtst.so")
    pisitools.dosym("/usr/lib32/libXtst.so.6.1.0","/usr/lib32/libXtst.so.6")
