#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    shelltools.copytree(".", "%s/usr/share/sabnzbd/" % get.installDIR())
    pisitools.dodoc("CHANGELOG.txt", "COPYRIGHT.txt", "GPL2.txt", "INSTALL.txt", "ISSUES.txt", "README.txt")
