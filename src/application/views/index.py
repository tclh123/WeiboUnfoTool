#!/usr/bin/env python
# -*- coding: utf-8 -*-

## as UnicodeDecodeError: 'ascii'...
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from application import app
from flask import Flask, render_template, session, request

from application.controllers import auth

@app.route('/', methods=['GET', 'POST'])
def index():

    client = auth._create_client()

    # 不在 新浪 访问的话没有 signed_request post参数
    try:
        data = client.parse_signed_request(request.form['signed_request'])
    except:
        return render_template('error.html', message="要在 http://apps.weibo.com/unfo 里访问哦亲。。")

    if data is None:
        raise StandardError('Error!')
    user_id = data.get('uid', '')
    auth_token = data.get('oauth_token', '')

    # 若post参数中没有 auth_token 等，则先进行授权
    if not user_id or not auth_token:
        return render_template('auth.html', client_id=auth.APP_KEY)

    expires = data.expires
    client.set_access_token(auth_token, expires)

    return render_template('index.html', context={ "name":"Harry" }, context2=auth.test())