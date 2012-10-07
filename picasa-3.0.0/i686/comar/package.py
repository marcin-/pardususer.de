#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system ("/usr/bin/download-picasa")

def preRemove():
    os.system ("/opt/google/picasa/3.0/uninstall")
