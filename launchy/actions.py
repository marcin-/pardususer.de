#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4

def setup():
  qt4.configure(parameters='-r Launchy.pro') 

def build():
  qt4.make()

def install():
  qt4.install()
