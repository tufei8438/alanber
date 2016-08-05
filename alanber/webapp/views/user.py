# coding:utf8

"""
Copyright 2016 Smallpay Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import json
import base64
from flask import Blueprint, render_template, request

from alanber.util import logger
from alanber.weixin.corp.oauth import authorize


bp = Blueprint('user', __name__)


@bp.route('/info')
@authorize
def info():
    user = json.loads(base64.b64decode(request.cookies.get('user')))
    is_follow = bool(request.cookies.get('is_follow'))
    return render_template('user/info.html', user=user, is_follow=is_follow)


@bp.route('/update')
@authorize
def update():
    if request.method == 'GET':
        return render_template('user/update.html')
    elif request.method == 'POST':
        return render_template('user/ok.html')