#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
WorkDir_PicasaInstallDir = ""+ get.workDIR() +"/opt/google/picasa/3.0/wine/drive_c/Program Files/Google/Picasa3/"
WorkDir_PicasaUpdateDir = ""+ get.workDIR() +"/picasa-"+ get.srcVERSION() +"-update/"

def setup():
    shelltools.system("rpm2targz -v %s/picasa-3.0-current.i386.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/picasa-3.0-current.i386.tar.gz --exclude=usr --exclude=opt/kde3 --exclude=opt/google/picasa/3.0/wine/drive_c/Program\ Files/Google/Picasa3" %get.workDIR())
    shelltools.chmod("%s/opt/google/picasa/3.0/bin/*" %get.workDIR())
    shelltools.chmod("%s/opt/google/picasa/3.0/bin/*" %get.workDIR())
    # extract Picasa udpate:
    shelltools.system("p7zip -d picasa-"+ get.srcVERSION() +"-update.7z")
    # copy content of Picasa update into Picasa Setup:
    shelltools.system("mkdir -v '"+ WorkDir_PicasaInstallDir +"'")
    shelltools.system("cp -Rfv "+ WorkDir_PicasaUpdateDir +"* '"+ WorkDir_PicasaInstallDir +"'")

def install():
#    pisitools.dosed("opt/google/picasa/3.0/bin/repackage32.sh","if [ \"`uname -m`\" != \"x86_64\" ] ; then","if [ \"`uname -m`\" = \"x86_64\" ] ; then" %get.installDIR())
    pisitools.dosed("opt/google/picasa/3.0/bin/repackage32.sh"," != "," = ")
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.dosym("/opt/google/picasa/3.0/bin/picasa", "/usr/bin/picasa")
    pisitools.dosym("/opt/google/picasa/3.0/lib/npPicasa3.so", "/usr/lib/browser-plugins/npPicasa3.so")
    pisitools.dosym("/opt/google/picasa/3.0/desktop/picasa-kdehal.desktop", "/usr/share/kde4/services/ServiceMenus/picasa-kdehal.desktop")