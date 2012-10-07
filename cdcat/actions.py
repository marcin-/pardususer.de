#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():   
    pisitools.dosed("src/cdcat.pro", "/local", "")
    qt4.configure(projectfile='src/cdcat.pro')

def build():
    qt4.make()

def install():
    qt4.install()
    for it in shelltools.ls("%s/usr/share/cdcat" % get.installDIR()):
        if it.endswith("png"): pisitools.dosym("/usr/share/cdcat/%s" % it, "/usr/share/pixmaps/%s" % it)
        else: pisitools.dosym("/usr/share/cdcat/%s" % it, "/usr/share/doc/cdcat/%s" % it)
    for f in shelltools.ls("src/lang/*.ts"):
        d = "%s/usr/share/locale/%s/LC_MESSAGES" % (get.installDIR(), f[15:17])
        shelltools.makedirs(d)
        shelltools.system('lrelease -qm %s/%s %s' % (d, f[9:].replace(".ts", ".qm"), f))

# By PiSiDo 2.0.0
