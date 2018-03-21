#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from click.testing import CliRunner

from oriole_test import oriole_test
from oriole_test import cli


@pytest.fixture
def response():
    pass


def test_content(response):
    pass


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Eric.Zhou' in result.output
