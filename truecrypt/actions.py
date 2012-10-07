#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="."
arch = "x86"
if get.ARCH() == "x86_64":
    arch = "x64"   

def install():
    pisitools.dobin("truecrypt-7.1-setup-" + arch)
    pisitools.dosym("/usr/bin/truecrypt-7.1-setup-" + arch,  "/usr/bin/truecrypt-setup")
