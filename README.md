# Python Autcomplete Function
David and Kyle's autocomplete project to practice Python.

User can enter the beginning of a word into command line to receive suggestions on how to finish the word. Autocomplete populates entire English dictionary into a tries data structure. 

Tech Stack: Python, Unittest

Follow these steps to try it out in the command line (make sure you have Python installed):

1. Clone the repository: git clone https://github.com/kheppenstall/autocomplete.git
1. `cd` into the directory `autocomplete`
1. Start an interpreter session by typing `python` in the command line.
1. Type the following commands into the irb session:
    
    ```python
    
    from trie import *
    trie = Trie()
    trie.populate('words.txt')    
    ```
1. Type `trie.suggest(fragment)` to see your suggested completions to the fragment.
(for example, `completion.suggest('aar') => ["aardwolf", "aardvark"]`

Follow these steps to run the tests:

1. Clone the repository: git clone https://github.com/kheppenstall/autocomplete.git
1. `cd` into the directory `autcomplete`
1. Install pytest: `pip install pytest` in the command line.
1. Run `pytest` in the command line to run test suite.
