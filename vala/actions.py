#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-vapigen")

def build():
    autotools.make()

def check():
     shelltools.cd("vapi")
     shelltools.sym("glib-2.0.vapi", "GLib-2.0.vapi")
     shelltools.sym("gobject-2.0.vapi", "GObject-2.0.vapi")
     shelltools.cd("..")
     autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("NEWS", "README", "AUTHORS", "COPYING")
