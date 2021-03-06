# encoding: utf-8
"""
Tests of io.asciisignalio
"""
from __future__ import absolute_import, division

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from ...io import MicromedIO
import numpy

from .common_io_test import BaseTestIO



class TestMicromedIO(BaseTestIO, unittest.TestCase, ):
    ioclass = MicromedIO
    files_to_test = [ 'File_micromed_1.TRC',
                            ]
    files_to_download = files_to_test


if __name__ == "__main__":
    unittest.main()
