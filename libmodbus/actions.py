#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.unlinkDir("%s/usr/share/man" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LESSER", "MIGRATION", "NEWS", "README.rst")
    pisitools.insinto("/usr/share/doc/libmodbus/html", "%s/%s/doc/*.html" % (get.workDIR(), get.srcDIR()))
    pisitools.insinto("/usr/share/libmodbus", "%s/%s/tests/*.c" % (get.workDIR(), get.srcDIR()))
    pisitools.insinto("/usr/share/libmodbus", "%s/%s/tests/README" % (get.workDIR(), get.srcDIR()))
