#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


#WorkDir="aegisub"
shelltools.export("HOME", get.workDIR()) 


def setup():
    shelltools.system("./autogen.sh --prefix=/usr --without-openal")
    
    # wxRE_ADVANCED does not work in wx-package of Pardus Linux, 
    # so replace it with wxRE_EXTENDED in several files .. ;-)
    # I found this solution by following thread:
    # http://www.fedoraforum.org/forum/showpost.php?p=1436852&postcount=10
    pisitools.dosed("./src/ass_dialogue.cpp","wxRE_ADVANCED","wxRE_EXTENDED")
    pisitools.dosed("./src/ass_time.cpp","wxRE_ADVANCED","wxRE_EXTENDED")
    pisitools.dosed("./src/dialog_search_replace.cpp","wxRE_ADVANCED","wxRE_EXTENDED")
    pisitools.dosed("./src/dialog_selection.cpp","wxRE_ADVANCED","wxRE_EXTENDED")
    pisitools.dosed("./src/subtitle_format_microdvd.cpp","wxRE_ADVANCED","wxRE_EXTENDED")
                                    
    autotools.configure("--without-hunspell \
                         --without-pulseaudio \
                         --without-alsa \
                         --without-openal")

def build():
    autotools.make()



def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")
