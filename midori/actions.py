#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# disable_ld_no_undefined is enable..
shelltools.export("JOBS", "5")
shelltools.export("CFLAGS", get.CFLAGS())
shelltools.export("CXXFLAGS", get.CXXFLAGS())
shelltools.export("LINKFLAGS", get.LDFLAGS())

def setup():
    shelltools.system("./waf configure \
                       --prefix=/usr \
                       --enable-nls \
                       --update-po \
                       --enable-docs \
                       --enable-apidocs  \
                       --enable-unique \
                       --enable-libnotify \
                       --enable-addons \
                       --disable-hildon")

def build():
    shelltools.system("./waf build")

def install():
    shelltools.system("./waf install --destdir=%s" % get.installDIR())
