#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 0775 /opt/desura/")
    os.system("/bin/chgrp users /opt/desura/")

    
def preRemove():
  # Delete .desktop files
  os.system("xdg-desktop-menu uninstall --mode user /opt/desura/desura.desktop /opt/desura/desura-force.desktop")

  # Delete old files
  os.system("rm -rf /opt/desura/.settings/!(cache|games|iteminfo_c.sqlite)")
  os.system("rm -rf /opt/desura/!(common|.settings)")