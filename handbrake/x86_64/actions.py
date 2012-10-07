#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."


def install():
    shelltools.system("rpm2targz handbrake-0.9.5-2mud2010.2.x86_64.rpm")
    shelltools.system("tar -zxvf handbrake-0.9.5-2mud2010.2.x86_64.tar.gz")
    pisitools.insinto("/", "usr")
    shelltools.system("rm -rf *")