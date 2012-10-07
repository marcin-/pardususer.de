#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="areca"

def install():
   
    pisitools.dosed("bin/areca_run.sh","JAVADIR=/usr/java","JAVADIR=/opt/sun-jdk/")
    shelltools.chmod("bin/areca*.sh",0755)
    shelltools.chmod("bin/run_tui.sh",0755)
    shelltools.chmod("areca*.sh",0755)
    pisitools.insinto("/opt/areca/","*")

