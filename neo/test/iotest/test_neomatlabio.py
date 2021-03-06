# encoding: utf-8
"""
Tests of io.asciisignalio
"""
from __future__ import absolute_import, division

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from ...io import NeoMatlabIO
import numpy

from .common_io_test import BaseTestIO

class TestNeoMatlabIO(BaseTestIO, unittest.TestCase):
    ioclass = NeoMatlabIO
    files_to_test = [ ]
    files_to_download = [ ]


if __name__ == "__main__":
    unittest.main()
