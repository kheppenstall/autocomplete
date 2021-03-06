import unittest
from node import *

class NodeTestCase(unittest.TestCase):

  def test_it_exists(self):
    assert Node('a')

  def test_node_stores_letter(self):
    node = Node('a')

    self.assertEqual('a', node.letter)

  def test_node_initializes_with_empty_links(self):
    node = Node('a')

    self.assertEqual({}, node.links)

  def test_node_set_links(self):
    node = Node('a')
    node.add_link('b')

    self.assertEqual('b', node.links['b'].letter)

  def test_node_terminator_defaults_to_false(self):
    node = Node('a')

    self.assertFalse(node.terminator)

  def test_node_terminator_set_to_true(self):
    node = Node('a')
    node.make_terminator()

    self.assertTrue(node.terminator)

  def test_node_stores_multiple_linkes(self):
    node = Node('a')
    node.add_link('b')
    node.links['b'].add_link('c')

    self.assertEqual('c', node.links['b'].links['c'].letter)

  def test_node_knows_if_it_includes_a_letter(self):
    node = Node('')
    node.add_link('b')
    
    self.assertTrue(node.includes_letter('b'))
    self.assertFalse(node.includes_letter('c'))

  def test_node_defaults_weight_to_zero(self):
    node = Node('c')

    self.assertEqual(0, node.weight)

  def test_node_increments_weights(self):
    node = Node('c')
    node.weight += 1

    self.assertEqual(1, node.weight)