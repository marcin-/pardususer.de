#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sh autogen.sh")
    autotools.configure("--enable-plugin_pulseaudio \
                         --enable-plugin_blowfish \
                         --enable-plugin_mcrypt \
                         --enable-gtkspell \
                         --enable-wine \
                         --disable-plugin_gpgme \
                         --disable-plugin_xmms \
                         --disable-rpath \
                         --disable-esd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "themes/gyachi-classic/gyach-icon_48.png", "gyachi.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps/gyachi", "themes/gyachi-classic/gyach-icon_32.png", "gyachi.png")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/gyachi", "themes/gyachi-classic/gyach-icon_48.png", "gyachi.png")

    pisitools.dodoc("ChangeLog", "VERSION", "doc/*.txt", "doc/txt/COPYING", "doc/txt/README", "doc/txt/webcams.txt", "doc/txt/gyachi-help-short.txt")
    pisitools.dohtml("doc/html/*")
