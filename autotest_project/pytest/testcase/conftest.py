#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import pytest
@pytest.fixture(scope='function',autouse=True)
def login():
    print('登录系统')
    yield
    print('退出系统')