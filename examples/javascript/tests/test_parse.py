# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import pytest

from tatsu.exceptions import TatSuException

import sandbojs
from .data import data_paths


@pytest.fixture()
def parser():
    return sandbojs.parser()


@pytest.fixture()
def datapaths():
    return data_paths()


def test_parse(parser, datapaths):
    for path in datapaths:
        with path.open() as f:
            contents = f.read()
        try:
            parser.parse(contents)
        except TatSuException as e:
            pytest.fail(str(e))
