﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools


#WorkDir="razor-qt-"+get.srcVERSION()


def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("README", "TODO", "CHANGELOG", "COPYING")