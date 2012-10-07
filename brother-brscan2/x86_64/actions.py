#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def install():

    shelltools.copytree("usr/bin", "%s/usr/bin" % get.installDIR())
    shelltools.copytree("usr/lib64", "%s/usr/lib" % get.installDIR())
    shelltools.copytree("usr/local", "%s/usr/local" % get.installDIR())
    
    pisitools.remove("/usr/bin/brsaneconfig2")
    pisitools.dosym("/usr/local/Brother/sane/brsaneconfig2","/usr/bin/brsaneconfig2")
    
    pisitools.remove("/usr/lib/libbrcolm2.so")
    pisitools.dosym("/usr/lib/libbrcolm2.so.1","/usr/lib/libbrcolm2.so")
    
    pisitools.remove("/usr/lib/libbrcolm2.so.1")
    pisitools.dosym("/usr/lib/libbrcolm2.so.1.0.1","/usr/lib/libbrcolm2.so.1")
    
    pisitools.remove("/usr/lib/libbrscandec2.so")
    pisitools.dosym("/usr/lib/libbrscandec2.so.1","/usr/lib/libbrscandec2.so")
    
    pisitools.remove("/usr/lib/libbrscandec2.so.1")
    pisitools.dosym("/usr/lib/libbrscandec2.so.1.0.0","/usr/lib/libbrscandec2.so.1")
    
    pisitools.remove("/usr/lib/sane/libsane-brother2.so")
    pisitools.dosym("/usr/lib/sane/libsane-brother2.so.1","/usr/lib/sane/libsane-brother2.so")
    
    pisitools.remove("/usr/lib/sane/libsane-brother2.so.1")
    pisitools.dosym("/usr/lib/sane/libsane-brother2.so.1.0.7","/usr/lib/sane/libsane-brother2.so.1")
