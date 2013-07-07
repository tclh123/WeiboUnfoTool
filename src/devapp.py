#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

'''
A WSGI app for dev.
'''

from application import app

if __name__ == "__main__":
    app.debug = True

    app.run(host='0.0.0.0', port=8888)