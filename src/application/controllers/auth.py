#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

from application.config import APP_KEY, APP_SECRET, CALLBACK_URL

from application.libs.weibo import APIError, APIClient

def test():
    return "test"

def _create_client(oauth_token=None, expires=None):
    client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL)
    if oauth_token and expires:
        client.set_access_token(oauth_token, expires)
    return client