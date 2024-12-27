
import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define the CFG for the given sentence
cfg_grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det AdjP N | Det N
  AdjP -> Adj AdjP | Adj
  VP -> V NP PP | V NP | V PP Conj VP
  PP -> P NP | P NP Conj NP | P Conj V
  Det -> 'the' | 'a'
  N -> 'dog' | 'cat'
  V -> 'barked' | 'chased' | 'chased away'
  P -> 'at' | 'away'
  Adj -> 'big' | 'black' | 'white'
  Conj -> 'and'
""")

# Create the parser with the modified grammar
parser = RecursiveDescentParser(cfg_grammar)

# The sentence from the 'Data_2.txt' file
sentence = 'The big black dog barked at the white cat and chased away'.lower().split()

# Generate and draw the parse trees for the sentence
trees = list(parser.parse(sentence))

# Since drawing the trees in Google Colab requires matplotlib, we use nltk's draw method
for tree in trees:
    tree.draw()
