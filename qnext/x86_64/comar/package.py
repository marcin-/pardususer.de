#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system ("/usr/bin/download-qnext")

def preRemove():
    os.system ("/opt/qnext/uninstall")
