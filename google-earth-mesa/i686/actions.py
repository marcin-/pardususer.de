#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/"]

def install():
    shelltools.system("export DISPLAY=")
    shelltools.system("sh GoogleEarthLinux.bin --target . --noexec")
    shelltools.makedirs("googleearth-linux-x86")
    shelltools.move("googleearth-linux-x86.tar", "%s/googleearth-linux-x86/" % get.workDIR())
    shelltools.cd("googleearth-linux-x86")
    shelltools.system("tar -xf googleearth-linux-x86.tar")
    shelltools.unlink("googleearth-linux-x86.tar")
    shelltools.makedirs("%s/usr/lib/googleearth" % get.installDIR())
    shelltools.copy("%s/googleearth-linux-x86/*" % get.workDIR(), "%s/usr/lib/googleearth/" % get.installDIR())

    shelltools.cd("..")
    shelltools.makedirs("googleearth-data")
    shelltools.move("googleearth-data.tar", "%s/googleearth-data/" % get.workDIR())
    shelltools.cd("googleearth-data")
    shelltools.system("tar -xf googleearth-data.tar")
    shelltools.unlink("googleearth-data.tar")
    shelltools.copy("%s/googleearth-data/*" % get.workDIR(), "%s/usr/lib/googleearth/" % get.installDIR())
   
    shelltools.system("chown -R root %s/usr/lib/googleearth/" % get.installDIR())
    shelltools.system("chgrp -R root %s/usr/lib/googleearth/" % get.installDIR())
    
    shelltools.cd("..")

    shelltools.makedirs("%s/usr/share/icons/hicolor/16x16/apps" % get.installDIR())
    shelltools.system("convert googleearth-icon.png -resize 16x16 googleearth.png")
    shelltools.move("googleearth.png", "%s/usr/share/icons/hicolor/16x16/apps/" % get.installDIR())
    
    shelltools.makedirs("%s/usr/share/icons/hicolor/32x32/apps" % get.installDIR())
    shelltools.system("convert googleearth-icon.png -resize 32x32 googleearth.png")
    shelltools.move("googleearth.png", "%s/usr/share/icons/hicolor/32x32/apps/" % get.installDIR())
    
    shelltools.makedirs("%s/usr/share/icons/hicolor/48x48/apps" % get.installDIR())
    shelltools.system("convert googleearth-icon.png -resize 48x48 googleearth.png")
    shelltools.move("googleearth.png", "%s/usr/share/icons/hicolor/48x48/apps/" % get.installDIR())
    
    pisitools.dosym("/lib/ld-linux.so.2", "/lib/ld-lsb.so.3")
    