from node import *

class Trie:

  def __init__(self):
    self.root = Node("")

  def insert(self, word):
    insertion = word
    current_node = self.root

    for letter in word: 
      insertion = insertion[1:]
      if not current_node.includes_letter(letter): current_node.add_link(letter)
      current_node = current_node.links[letter]
      if len(insertion) == 0: current_node.make_terminator()


  def find_words(self, fragment = '', node = None):
    words = []
    if not node: node = self.root

    for letter, next_node in node.links.items():
      if next_node.terminator: words.append(fragment + letter)

      for word in self.find_words(fragment + letter, next_node):
        words.append(word)

    return words

  def suggest(self, fragment):
    node = self.node_finder(fragment)
    return self.find_words(fragment, node)

  def node_finder(self, fragment, node = None,):
    if not node: node = self.root

    if node.includes_letter(fragment[0]):
      next_node = node.links[fragment[0]]
      if len(fragment) == 1: return next_node
      node_finder(fragment[1:], next_node)
    else: return None

  def populate(self, file):
    dictionary_file = open(file, 'r')
    for word in dictionary_file.readlines():
      self.insert(word)
