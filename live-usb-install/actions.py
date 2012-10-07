#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="."


def install():
    pisitools.dodir("/usr/share/live-usb-install")
    pisitools.dodir("/usr/share/pixmaps")
    pisitools.dodir("/usr/share/applications")

    pisitools.insinto("/usr/share/live-usb-install", "asubprocess.py", "asubprocess.py")
    pisitools.insinto("/usr/share/live-usb-install", "backg.png", "backg.png")
    pisitools.insinto("/usr/share/live-usb-install", "grub.exe", "grub.exe")
    pisitools.insinto("/usr/share/live-usb-install", "live-usb-install.glade", "live-usb-install.glade")
    pisitools.insinto("/usr/share/live-usb-install", "live-usb-install.py", "live-usb-install.py")
    pisitools.insinto("/usr/share/live-usb-install", "logo.png", "logo.png")
    pisitools.insinto("/usr/share/live-usb-install", "menu.lst", "menu.lst")
    pisitools.insinto("/usr/share/live-usb-install", "syslinux-custom.cfg", "syslinux-custom.cfg")
    pisitools.insinto("/usr/share/live-usb-install", "syslinux.mbr", "syslinux.mbr")
    pisitools.insinto("/usr/share/live-usb-install", "syslinux-wingrub.cfg", "syslinux-wingrub.cfg")
    pisitools.insinto("/usr/share/live-usb-install", "vesamenu.c32", "vesamenu.c32")
    pisitools.insinto("/usr/share/live-usb-install", "wingrub-menu.lst", "wingrub-menu.lst")
    
    shelltools.copytree("presets", "%s/usr/share/live-usb-install/" % get.installDIR())
    shelltools.copytree("pyudev", "%s/usr/share/live-usb-install/" % get.installDIR())
    shelltools.copytree("locale", "%s/usr/share/live-usb-install/" % get.installDIR())
    
    pisitools.insinto("/usr/share/pixmaps", "logo.png", "live-usb-install.png")
