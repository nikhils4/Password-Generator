# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:16:14 2018

@author: Snik
"""

from distutils.core import setup
import py2exe
setup(
       console=['passw_gen.py'],
       options = {
               py2exe:{
                       'packages': ['os','random','os.path','pyperclip','time','pydrive.auth','pydrive.drive']}})