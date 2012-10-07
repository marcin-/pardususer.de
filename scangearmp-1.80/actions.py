#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WORKDIR = "%s-1" % get.srcDIR()
model_numbers = ("386", "387", "388", "389", "390", "391", "393")
arch_bit = "32" if get.ARCH() == "i686" else "64"

def setup():
    shelltools.cd("scangearmp")
    shelltools.system("./autogen.sh --prefix=/%s --enable-libpath=/%s/lib LDFLAGS=\"-L`pwd`/../com/libs_bin%s\"" % (get.defaultprefixDIR(), get.defaultprefixDIR(), arch_bit))

def build():
    shelltools.cd("scangearmp")
    # force to use libtool from system
    shelltools.unlink("ltmain.sh")
    shelltools.unlink("libtool")
    shelltools.system("ln -s `which libtool` .")
    # make as usual
    autotools.make()

def install():
    for model in model_numbers:
        pisitools.insinto("/%s/lib/bjlib" % get.defaultprefixDIR(), "%s/*.tbl" % model)
        pisitools.insinto("/%s/lib/bjlib" % get.defaultprefixDIR(), "%s/*.DAT" % model)
        pisitools.dolib("%s/libs_bin%s/*.so" % (model, arch_bit))
    pisitools.dolib("com/libs_bin%s/*.so" %  arch_bit)
    #shelltools.chmod("com/ini/canon_mfp_net.ini", 0644)
    #pisitools.insinto("/%s/lib/bjlib" % get.defaultprefixDIR(), "com/ini/canon_mfp_net.ini")

    pisitools.dodoc("LICENSE*", "scangearmp/AUTHORS", "scangearmp/ChangeLog", "scangearmp/LICENSE", "scangearmp/NEWS", "scangearmp/COPYING")

    shelltools.cd("scangearmp")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/%s/udev/rules.d/" % get.confDIR(), "etc/*.rules")
    pisitools.dosym("/%s/bin/scangearmp" % get.defaultprefixDIR(), "/usr/lib/gimp/2.0/plug-ins/scangearmp")
