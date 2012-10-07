#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get


#WorkDir="synfigstudio-0.62.02-20101113.master.1.i386"  evtl nicht notwendig?

def install():
    pisitools.insinto("/usr/","bin")

    pisitools.insinto("/opt/synfig/","etc")
    pisitools.insinto("/opt/synfig/","lib")
    pisitools.insinto("/opt/synfig/","share")

    #pisitools.docdoc("AUTHORS","README","COPYING","NEWS")