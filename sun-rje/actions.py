#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.util import run_batch, check_file_hash, Error

WorkDir = get.ARCH()
NoStrip = "/"
Name = "6u34"
BinName = "jdk-%s-linux-%s.bin" % (Name, get.ARCH().replace("i6", "i5").replace("86_", ""))
UrlName = "http://download.oracle.com/otn-pub/java/jdk/6u34-b04/%s" % BinName
Arch = "amd64" if get.ARCH() == "x86_64" else "i586"

def setup():
    if not shelltools.isFile(BinName):
        shelltools.system('/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -o %s %s  --header "Cookie:oraclelicensejdk-%s-oth-JPR=accept-securebackup-cookie;gpw_e24=http://edelivery.oracle.com"' % (BinName, UrlName, Name))
    hash = run_batch("cat jdk-6u34-linux-%s.bin.sha1" % Arch)[1].split()[0]
    if not check_file_hash(BinName, hash): raise Error("Wrong sha1sum.")
    shelltools.makedirs("unbundle-jdk")
    shelltools.cd("unbundle-jdk")
    shelltools.system("sh ../%s --noregister" % BinName)

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct unbundle-jdk %s/opt/sun-jdk %s/opt/sun-jre"% (get.installDIR(),get.installDIR()))

    pisitools.dodir("/usr/lib/browser-plugins")

    # Next generation Java plugin is needed by Firefox 3.6+
    # http://java.sun.com/javase/6/webnotes/install/jre/manual-plugin-install-linux.html
    pisitools.dosym("/opt/sun-jre/lib/%s/libnpjp2.so" % Arch.replace("i586", "i386"), "/usr/lib/browser-plugins/javaplugin.so")

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "THIRDPARTYLICENSEREADME.txt",
                "register.html", "register_ja.html", "register_zh_CN.html"]:
        file = "%s/opt/sun-jdk/%s" % (get.installDIR(), doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)

    # Bug #18115
    if Arch == "amd64":
        pisitools.remove("/opt/sun-jdk/man/ja_JP.eucJP/man1/javaws.1")
        #additional missing links to man file
        pisitools.remove("/opt/sun-jdk/man/ja_JP.eucJP/man1/kinit.1")
        pisitools.remove("/opt/sun-jdk/man/ja_JP.eucJP/man1/klist.1")
        pisitools.remove("/opt/sun-jdk/man/ja_JP.eucJP/man1/ktab.1")
