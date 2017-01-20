import unittest
from node import *

class NodeTestCase(unittest.TestCase):

  def test_it_exists(self):
    assert Node('a')