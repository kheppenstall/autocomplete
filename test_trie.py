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


  def test_it_can_take_fragment_and_give_recomendations(self):
    trie = Trie()
    trie.insert('pi')
    trie.insert('pizza')
    trie.insert('a')
    words = sorted(trie.suggest("p"))

    self.assertEqual(['pi', 'pizza'], words)

  def test_it_populates_file(self):
    trie = Trie()
    trie.populate('words.txt')

    self.assertEqual(235886, len(trie.find_words()))