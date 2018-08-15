#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oriole_api.json import success, fail


def test_success():
    data = {"data": 1}
    result = success("", data)
    assert result["result"]["data"] == 1


def test_fail():
    result = fail("", "auth_fail")
    assert result["detail"] == "auth_fail"
