class Node:
  def __init__(self, letter):
    self.letter = letter
    self.links = {}
    self.terminator = False

  def add_link(self, letter):
    self.links[letter] = Node(letter)

  def make_terminator(self):
    self.terminator = True

  def includes_letter(self, letter):
    return letter in list(self.links.keys())

