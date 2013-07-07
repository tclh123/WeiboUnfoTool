#!/usr/bin/env python
#-*-coding:utf-8-*-

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

from application import app
from flask import Flask, render_template, session, request

@app.route('/')
def index():
    return render_template('index.html')