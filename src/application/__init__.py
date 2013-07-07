#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '0.1'
__author__ = 'tclh123'

from flask import Flask
app = Flask(__name__)

from application.views import *
