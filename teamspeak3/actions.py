#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

#WorkDir="teamspeak3-beta36-client-linux_x86"

def install():
    pisitools.dodoc("CHANGELOG","LICENSE")
    pisitools.insinto("/opt/teamspeak3/","*")