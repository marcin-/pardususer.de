#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #fix prefix
    pisitools.dosed("Makefile", "(prefix=)(\/usr)\/local", r"\1%s\2" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall()
