#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

# $APPBINPATH = "%s/usr/bin__"  % get.installDIR()
# $DESKTOPPATH = "%s/usr/share/applications__"  % get.installDIR()
# $SRCPATH = "%s__" % get.workDIR()
# $TMDESKTOP = "%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR()
# $APPPATH = /usr/share/office2008
# $THEMEDIR = "%s/usr/share/icons/gnome__" % get.installDIR()
# $GMIMEPATH = "%s/usr/share/mime-info__" % get.installDIR()
# $MIMEPATH = "%s/usr/share/mime__" % get.installDIR()
# $KMIMEPATH = "%s/usr/kde/4/share/mimelnk__" % get.installDIR()
# $DATADIR = "%s/usr/share__" % get.installDIR()

def setup():
    shelltools.makedirs("office2008")
    shelltools.move("office.tgz", "%s/office2008/" % get.workDIR())
    shelltools.cd("office2008")
    shelltools.system("tar -xf office.tgz")
    shelltools.unlink("office.tgz")

def install():
#create_script(textmaker)
    shelltools.makedirs("%s/usr/bin" % get.installDIR())
    shelltools.touch("%s/usr/bin/textmaker"  % get.installDIR())
    shelltools.echo("%s/usr/bin/textmaker"  % get.installDIR(), "#!/bin/sh")
    shelltools.echo("%s/usr/bin/textmaker"  % get.installDIR(), "# A script to run TextMaker.")
    shelltools.echo("%s/usr/bin/textmaker"  % get.installDIR(), "\"/usr/share/office2008\"/textmaker \"$@\"")
    shelltools.chmod("%s/usr/bin/textmaker"  % get.installDIR(), 0755)
#create_script(planmaker)
    shelltools.makedirs("%s/usr/bin" % get.installDIR())
    shelltools.touch("%s/usr/bin/planmaker"  % get.installDIR())
    shelltools.echo("%s/usr/bin/planmaker"  % get.installDIR(), "#!/bin/sh")
    shelltools.echo("%s/usr/bin/planmaker"  % get.installDIR(), "# A script to run PlanMaker.")
    shelltools.echo("%s/usr/bin/planmaker"  % get.installDIR(), "\"/usr/share/office2008\"/planmaker \"$@\"")
    shelltools.chmod("%s/usr/bin/planmaker"  % get.installDIR(), 0755)
#create_script(softmaker)
    shelltools.touch("%s/usr/bin/presentations"  % get.installDIR())
    shelltools.echo("%s/usr/bin/presentations"  % get.installDIR(), "#!/bin/sh")
    shelltools.echo("%s/usr/bin/presentations"  % get.installDIR(), "# A script to run SoftMaker Presentations.")
    shelltools.echo("%s/usr/bin/presentations"  % get.installDIR(), "\"/usr/share/office2008\"/presentations \"$@\"")
    shelltools.chmod("%s/usr/bin/presentations"  % get.installDIR(), 0755)

#create_desktop(textmaker)
    shelltools.makedirs("%s/usr/share/applications" % get.installDIR())
    shelltools.copy("%s/office2008/mime/tml.dsk" % get.workDIR(), "%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR())
    shelltools.chmod("%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR(), 0644)
    shelltools.echo("%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR(), "Icon=/usr/share/office2008/icons/tml_48.png")
    shelltools.echo("%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR(), "TryExec=/usr/share/office2008/textmaker")
    shelltools.echo("%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR(), "Exec=/usr/share/office2008/textmaker")
    shelltools.echo("%s/usr/share/applications/textmaker-2008.desktop" % get.installDIR(), "Path=/usr/share/office2008")

#create_desktop(planmaker)
    shelltools.copy("%s/office2008/mime/pml.dsk" % get.workDIR(), "%s/usr/share/applications/planmaker-2008.desktop" % get.installDIR())
    shelltools.chmod("%s/usr/share/applications/planmaker-2008.desktop" % get.installDIR(), 0644)
    shelltools.echo("%s/usr/share/applications/planmaker-2008.desktop" % get.installDIR(), "Icon=/usr/share/office2008/icons/pml_48.png")
    shelltools.echo("%s/usr/share/applications/planmaker-2008.desktop" % get.installDIR(), "TryExec=/usr/share/office2008/planmaker")
    shelltools.echo("%s/usr/share/applications/planmaker-2008.desktop" % get.installDIR(), "Exec=/usr/share/office2008/planmaker")
    shelltools.echo("%s/usr/share/applications/planmaker-2008.desktop" % get.installDIR(), "Path=/usr/share/office2008")

#create_desktop(presentations)
    shelltools.copy("%s/office2008/mime/prl.dsk" % get.workDIR(), "%s/usr/share/applications/presentations-2008.desktop" % get.installDIR())
    shelltools.chmod("%s/usr/share/applications/presentations-2008.desktop" % get.installDIR(), 0644)
    shelltools.echo("%s/usr/share/applications/presentations-2008.desktop" % get.installDIR(), "Icon=/usr/share/office2008/icons/prl_48.png")
    shelltools.echo("%s/usr/share/applications/presentations-2008.desktop" % get.installDIR(), "TryExec=/usr/share/office2008/presentations")
    shelltools.echo("%s/usr/share/applications/presentations-2008.desktop" % get.installDIR(), "Exec=/usr/share/office2008/presentations")
    shelltools.echo("%s/usr/share/applications/presentations-2008.desktop" % get.installDIR(), "Path=/usr/share/office2008")

#copy_icons()
    shelltools.makedirs("%s/usr/share" % get.installDIR())
    shelltools.makedirs("%s/usr/share/icons/hicolor/48x48/mimetypes" % get.installDIR())
    shelltools.makedirs("%s/usr/share/icons/hicolor/32x32/mimetypes" % get.installDIR())
    shelltools.makedirs("%s/usr/share/icons/hicolor/16x16/mimetypes" % get.installDIR())
#tmd
    shelltools.copy("%s/office2008/icons/tmd_48.png" % get.workDIR(), "%s/usr/share/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-tmd.png" % get.installDIR())
    shelltools.copy("%s/office2008/icons/tmd_32.png" % get.workDIR(), "%s/usr/share/icons/hicolor/32x32/mimetypes/gnome-mime-application-x-tmd.png" % get.installDIR())
    shelltools.copy("%s/office2008/icons/tmd_16.png" % get.workDIR(), "%s/usr/share/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-tmd.png" % get.installDIR())
#pmd
    shelltools.copy("%s/office2008/icons/pmd_48.png" % get.workDIR(), "%s/usr/share/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-pmd.png" % get.installDIR())
    shelltools.copy("%s/office2008/icons/pmd_32.png" % get.workDIR(), "%s/usr/share/icons/hicolor/32x32/mimetypes/gnome-mime-application-x-pmd.png" % get.installDIR())
    shelltools.copy("%s/office2008/icons/pmd_16.png" % get.workDIR(), "%s/usr/share/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-pmd.png" % get.installDIR())
#prd
    shelltools.copy("%s/office2008/icons/prd_48.png" % get.workDIR(), "%s/usr/share/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-prd.png" % get.installDIR())
    shelltools.copy("%s/office2008/icons/prd_32.png" % get.workDIR(), "%s/usr/share/icons/hicolor/32x32/mimetypes/gnome-mime-application-x-prd.png" % get.installDIR())
    shelltools.copy("%s/office2008/icons/prd_16.png" % get.workDIR(), "%s/usr/share/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-prd.png" % get.installDIR())

#create_mime()
    shelltools.makedirs("%s/usr/share/mime/packages" % get.installDIR())
    shelltools.copy("%s/office2008/mime/smoffice.xml" % get.workDIR(), "%s/usr/share/mime/packages" % get.installDIR())
    shelltools.chmod("%s/usr/share/mime/packages/smoffice.xml" % get.installDIR(), 0644)
#tm
    shelltools.makedirs("%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.copy("%s/office2008/mime/x-tmd.desktop" % get.workDIR(), "%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.copy("%s/office2008/mime/x-tmv.desktop" % get.workDIR(), "%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.chmod("%s/usr/share/mimelnk/application/x-tmd.desktop" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/mimelnk/application/x-tmv.desktop" % get.installDIR(), 0644)
#pm
    shelltools.copy("%s/office2008/mime/x-pmd.desktop" % get.workDIR(), "%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.copy("%s/office2008/mime/x-pmv.desktop" % get.workDIR(), "%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.chmod("%s/usr/share/mimelnk/application/x-pmd.desktop" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/mimelnk/application/x-pmv.desktop" % get.installDIR(), 0644)    
#pr
    shelltools.copy("%s/office2008/mime/x-prd.desktop" % get.workDIR(), "%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.copy("%s/office2008/mime/x-prv.desktop" % get.workDIR(), "%s/usr/share/mimelnk/application" % get.installDIR())
    shelltools.chmod("%s/usr/share/mimelnk/application/x-prd.desktop" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/mimelnk/application/x-prv.desktop" % get.installDIR(), 0644)

#copylinks
    pisitools.dosym("/usr/share/office2008/icons/prd_48.png", "/usr/share/pixmaps/prd.png")
    pisitools.dosym("/usr/share/office2008/icons/prl_48.png", "/usr/share/pixmaps/prl.png")
    pisitools.dosym("/usr/share/office2008/icons/pmd_48.png", "/usr/share/pixmaps/pmd.png")
    pisitools.dosym("/usr/share/office2008/icons/pml_48.png", "/usr/share/pixmaps/pml.png")
    pisitools.dosym("/usr/share/office2008/icons/tmd_48.png", "/usr/share/pixmaps/tmd.png")
    pisitools.dosym("/usr/share/office2008/icons/tml_48.png", "/usr/share/pixmaps/tml.png")

    shelltools.makedirs("%s/usr/share" % get.installDIR())
    shelltools.copytree("office2008", "%s/usr/share/office2008/" % get.installDIR())
   