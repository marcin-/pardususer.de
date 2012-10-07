#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

configure_args = "--with-lib32=lib32 --with-lib64=lib" if get.ARCH() == "x86_64" else ""

def setup():
    autotools.rawConfigure(configure_args)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog*", "COPYING", "NEWS", "README", "TODO")
