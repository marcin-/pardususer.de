#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."


def setup():
    shelltools.system("rpm2targz -v %s/rpm-utils-4.5-54.i686.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/rpm-utils-4.5-54.i686.tar.gz --exclude=lib" %get.workDIR())

def install():
    pisitools.insinto("/usr/bin/", "./usr/bin/rpm2cpio")
    pisitools.insinto("/usr/share/man/man8/","./usr/share/man/man8/rpm2*")
    pisitools.insinto("/usr/share/man/ja/man8/","./usr/share/man/ja/man8/rpm2*")
    pisitools.insinto("/usr/share/man/ko/man8/","./usr/share/man/ko/man8/rpm2*")
    pisitools.insinto("/usr/share/man/pl/man8/","./usr/share/man/pl/man8/rpm2*")
    pisitools.insinto("/usr/share/man/ru/man8/","./usr/share/man/ru/man8/rpm2*")
