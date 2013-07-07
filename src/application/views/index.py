#!/usr/bin/env python
#-*-coding:utf-8-*-

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

from application import app
from flask import Flask, render_template, session, request

from application.controllers import testWeiboApi

@app.route('/')
def index():

    return render_template('index.html', context={ "name":"Harry" }, context2=testWeiboApi.test())