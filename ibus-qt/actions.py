# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure()

def build():
    cmaketools.make("LIBS=%s" % get.LDFLAGS())

def install():
    cmaketools.install()
    pisitools.removeDir('/usr/share/doc/%s-%s' % (get.srcNAME(),  get.srcVERSION()))
    pisitools.dodoc("AUTHORS", "COPYING", "README", "TODO")
