#!/usr/bin/env python
# -*- coding: utf-8 -*-

## as UnicodeDecodeError: 'ascii'...
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from application import app
from flask import Flask, render_template, session, request

from application.controllers import auth
from application.controllers.user import _from_weibo_user


@app.route('/', methods=['GET', 'POST'])
def index():

    client = auth._create_client()

    # 不在 新浪 访问的话没有 signed_request post参数        #TODO dict.has_key() ？ or xxx in dict ? or dict.get('key', 'default value') ?
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

    # 若post参数中有 auth_token，则 set 到 client
    expires = data.expires
    client.set_access_token(auth_token, expires)

    # Call Api
    u = client.users.show.get(uid=user_id)
    user = _from_weibo_user(u)
    friends = client.friendships.friends.ids.get(count=5000)

    return render_template('index.html', user=user, friends = friends)
    # 保留 signed_request=request.form['signed_request'] ？还是session，cookie什么的？