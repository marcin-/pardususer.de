#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="x264-snapshot-20120220-2245" % get.srcVERSION().split("_")
verMAJOR = "0"
verMINOR = "0"


def getMinorVersion():
    f = file("x264.h").read()
    for i in f.split("\n"):
        if i.startswith("#define X264_BUILD"):
            return i.split()[-1]

    return "0"

def setup():
    shelltools.export("CFLAGS", "%s -O3" % get.CFLAGS())

    # force using shared gpac
    pisitools.dosed("configure", "-lgpac_static", "-lgpac")

    # these disables are here to prevent circular deps, especially with ffmpeg
    autotools.rawConfigure("--prefix=/usr \
                            --enable-pic \
                            --disable-avs \
                            --disable-ffms \
                            --disable-swscale \
                            --disable-lavf \
                            --enable-shared")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dosym("/usr/lib/libx264.so.120", "/usr/lib/libx264.so.115")

    #verMINOR = getMinorVersion()
    #pisitools.dosym("libx264.so.%s.%s" % (verMAJOR, verMINOR), "/usr/lib/libx264.so.%s" % verMAJOR)

    # No static libs
