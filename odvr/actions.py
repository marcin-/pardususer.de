# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.doexe('odvr',  '/usr/bin')
    pisitools.doexe('odvr-gui',  '/usr/bin')
    pisitools.insinto('/etc/udev/rules.d',  '41-odvr.rules')
    pisitools.dodoc("COPYING", "README")
