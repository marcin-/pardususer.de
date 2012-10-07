#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]

def install():
    pisitools.copytree("usr", "%s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/libcnbpcmcm327.so.6.61.1", "/usr/lib/libcnbpcmcm327.so.6")
    pisitools.dosym("/usr/lib/libcnbpcmcm327.so.6.61.1", "/usr/lib/libcnbpcmcm327.so")
    pisitools.dosym("/usr/lib/libcnbpcnclapi327.so.3.3.0", "/usr/lib/libcnbpcnclapi327.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclapi327.so.3.3.0", "/usr/lib/libcnbpcnclapi327.so")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd327.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd327.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd327.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd327.so")
    pisitools.dosym("/usr/lib/libcnbpcnclui327.so.3.3.0", "/usr/lib/libcnbpcnclui327.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclui327.so.3.3.0", "/usr/lib/libcnbpcnclui327.so")
    pisitools.dosym("/usr/lib/libcnbpess327.so.3.0.9", "/usr/lib/libcnbpess327.so.3")
    pisitools.dosym("/usr/lib/libcnbpess327.so.3.0.9", "/usr/lib/libcnbpess327.so")
    pisitools.dosym("/usr/lib/libcnbpo327.so.1.0.3", "/usr/lib/libcnbpo327.so.1")
    pisitools.dosym("/usr/lib/libcnbpo327.so.1.0.3", "/usr/lib/libcnbpo327.so")
