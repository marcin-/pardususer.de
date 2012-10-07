#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# You can use these as variables, they will replace GUI values before build.
# Package Name : vnstat
# Version : 1.11
# Summary : A console-based network traffic monitor

# If the project that you are tying to compile is in a sub directory in the 
# source archive, than you can define working directory. For example; 
# WorkDir="vnstat-"+ get.srcVERSION() +"/sub_project_dir/"

#def setup():
    #autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "COPYING", "FAQ", "README")
