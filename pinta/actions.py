#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#configDir = '/root/.config'
#if shelltools.isLink(configDir) : shelltools.unlink(configDir)
#elif shelltools.isDirectory(configDir) : shelltools.unlinkDir(configDir)
#shelltools.makedirs(get.workDIR())
#shelltools.system('ln -s %s %s' % (get.workDIR(), configDir))

#shelltools.export("MONO_SHARED_DIR", get.workDIR())
shelltools.export("XDG_CONFIG_HOME", get.workDIR())


def setup():
    autotools.configure()
    
def build():
    autotools.make()
    
def install():
    autotools.install()
    pisitools.dodoc("*.txt")

