import unittest
from trie import *

class TrieTestCase(unittest.TestCase):

  def test_it_initializes_with_a_root_node(self):
    trie = Trie()

    self.assertEqual("",trie.root.letter)

  def test_it_inserts_a_one_letter_word(self):
    trie = Trie()
    trie.insert('a')

    self.assertTrue(trie.root.includes_letter('a'))
    self.assertTrue(trie.root.links['a'].terminator)

  def test_it_inserts_a_two_letter_word(self):
    trie = Trie()
    trie.insert('ab')

    self.assertTrue(trie.root.includes_letter('a'))
    self.assertFalse(trie.root.terminator)
    self.assertTrue(trie.root.links['a'].includes_letter('b'))
    self.assertTrue(trie.root.links['a'].links['b'].terminator)

  def test_it_knows_its_words(self):
    trie = Trie()
    trie.insert('pi')
    trie.insert('pizza')
    trie.insert('a')
    words = sorted(trie.find_words())

    self.assertEqual(['a', 'pi', 'pizza'], words)

  def test_it_can_take_letter_and_give_recomendations(self):
    trie = Trie()
    trie.insert('pi')
    trie.insert('pizza')
    trie.insert('a')
    words = sorted(trie.suggest('p'))

    self.assertEqual(['pi', 'pizza'], words)

  def test_it_can_take_fragment_and_give_recomendations(self):
    trie = Trie()
    trie.insert('pi')
    trie.insert('pizza')
    trie.insert('a')
    words = sorted(trie.suggest('pi'))

    self.assertEqual(['pizza'], words)

  def test_it_recommends_empty_list_with_no_recommendations(self):
    trie = Trie()
    trie.insert('p')
    words = trie.suggest('pi')

    self.assertEqual([], words)

  def test_it_recommends_empty_list_with_no_words_in_trie(self):
    trie = Trie()
    words = trie.suggest('pi')

    self.assertEqual([], words)

  # def test_it_populates_file(self):
  #   trie = Trie()
  #   trie.populate('words.txt')

  #   self.assertEqual(235886, len(trie.find_words()))  

  def test_it_increments_weight_when_letter_is_inserted_multiple_times(self):
    trie = Trie()
    trie.insert('a')
    trie.insert('a')

    self.assertEqual(2, trie.root.links['a'].weight)

  def test_it_increments_weight_when_word_is_inserted_multiple_times(self):
    trie = Trie()
    trie.insert('pizza')
    trie.insert('pizza')
    node = trie.node_finder('pizza')

    self.assertEqual(2, node.weight)

  def test_it_suggests_words_based_on_weight(self):
    trie = Trie()
    trie.insert('pizza')
    trie.insert('pizza')
    trie.insert('pizza')
    trie.insert('pi')
    trie.insert('pi')
    trie.insert('pizzas')

    self.assertEqual(['pizza', 'pi', 'pizzas'], trie.suggest('p'))


