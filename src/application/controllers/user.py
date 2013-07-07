#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

def _from_weibo_user(user):
    return dict(\
        name = user.name,\
        gender = user.get('gender', ''),\
        city = user.get('city', ''),\
        province = user.get('province', ''),\
        image_url = user.get('image_url', ''),\
        profile_image_url = user.get('profile_image_url', ''),\
        avatar_large = user.get('avatar_large', ''),\
        statuses_count = user.get('statuses_count', 0),\
        friends_count = user.get('friends_count', 0),\
        followers_count = user.get('followers_count', 0),\
        verified = user.get('verified', False),\
        verified_type = user.get('verified_type', 0),\
    )