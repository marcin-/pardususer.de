#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

# Package Name : easycrypt
# Version : 2.3.2
# Summary : Simply a Graphical GUI of the simplest nature for the Security Command Line product TrueCrypt.

WorkDir="easycrypt"

def install():
    pisitools.dodoc("ChangeLog", "copyright", "README")
    pisitools.dobin("easycrypt")
    pisitools.insinto("/usr/share/applications", "easycrypt.desktop")
    pisitools.insinto("/usr/share/easycrypt", "EasyCrypt*")
    pisitools.insinto("/usr/share/easycrypt", "icons")
    pisitools.insinto("/usr/share/easycrypt", "locale")
    pisitools.insinto("/usr/share/pixmaps", "icons/easycrypt.*")