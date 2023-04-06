# -*- coding: utf-8 -*-

import unittest
from genetic_algorithm_neural_network_training import *

class BasicTestSuite(unittest.TestCase):
    """
    Test cases here...
    """

    def test_main(self):
        self.assertEquals(main(), "Hello World")
