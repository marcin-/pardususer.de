#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."


def setup():
    # The source archive of this package contains only ZIP files - so we've to to do:
    # 1. Changing to the work directory of this package: cd /var/pisi/pdfsam-enhanced-xxx/work/
    # 2. Extracting all ZIP files in the work directory: for zipfile in *.zip;do unzip "$zipfile"; done
    shelltools.system("cd '"+ get.workDIR() +"' && for zipfile in *.zip;do unzip \"$zipfile\"; done")

    # Edit the build-properties (see also http://www.pdfsam.org/bbforum/viewtopic.php?f=2&t=753&start=0)
    pisitools.dosed("pdfsam-maine/ant/build.properties","pdfsam.deploy.dir=/home/torakiki/tmp","pdfsam.deploy.dir=../build/pdfsam-maine")
    pisitools.dosed("pdfsam-maine/ant/build.properties","workspace.dir=/media/LACIE/pdfsam/workspace-enhanced","workspace.dir=../")
    pisitools.dosed("pdfsam-maine/ant/build.properties","build.dir=/media/LACIE/build-2","build.dir=../build")


def build():
    shelltools.system("cd '"+ get.workDIR() +"/pdfsam-maine/ant/' && JAVA_HOME=/opt/sun-jdk/; export JAVA_HOME; ant cleanAll")
    shelltools.system("cd '"+ get.workDIR() +"/pdfsam-maine/ant/' && JAVA_HOME=/opt/sun-jdk/; export JAVA_HOME; ant dist")


def install():
    pisitools.insinto("/opt/pdfsam-enhanced/", "build/pdfsam-maine/release/dist/pdfsam-enhanced/*")
    pisitools.insinto("/usr/share/doc/pdfsam-enhanced/","build/pdfsam-maine/release/dist/pdfsam-enhanced/doc/*")