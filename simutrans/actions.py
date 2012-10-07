# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = '.'
sname = get.srcNAME()

def chmod(path):
    shelltools.chmod(path,  mode = 0755)
    for f in shelltools.ls(path):
        path2f = '/'.join((path,  f))
        if shelltools.isFile(path2f):
            shelltools.chmod(path2f,  mode = 0644)
        else:
            chmod(path2f)

def setup():
    shelltools.system('cp config.template config.default')
    shelltools.system('convert %s.ico -alpha on %s.png' % (sname,  sname))
    chmod('%s/simutrans' %  get.workDIR())

def build():
    autotools.make()

def install():
    pisitools.dobin('build/default/sim')
    pisitools.rename('/usr/bin/sim',  sname)
    for f in ["config", "font", "music", "pak", "skin", "text"]:
        pisitools.insinto('/usr/share/%s' % sname,  '/'.join((sname,  f)))
    pisitools.insinto('/usr/share/pixmaps',  '%s.png' % sname)
    pisitools.dodoc('%s/*.txt' % sname)
