#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s/.dropbox-dist" % get.ARCH()
NoStrip = "/opt/dropbox/library.zip"

def install():
    pisitools.dodir("/opt/dropbox")
    pisitools.insinto("/opt/dropbox", "*")
    pisitools.dodoc("ACKNOWLEDGEMENTS", "VERSION")
    pisitools.remove("/opt/dropbox/ACKNOWLEDGEMENTS")
    pisitools.remove("/opt/dropbox/VERSION")
