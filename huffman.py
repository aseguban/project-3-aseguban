from array_list import *

# a HuffmanTree is one of
# - a HuffmanNode()
# - Leaf

class Leaf:
   def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __eq__(self, other):
        return ((type(other) == Leaf)
          and self.char == other.char
          and self.freq == other.freq
        )

    def __repr__(self):
        return ("Leaf({!r}, {!r})".format(self.char, self.freq))

class HuffmanNode:
   def __init__(self, val, occ):
        self.val = val
        self.occ = occ

    def __eq__(self, other):
        return ((type(other) == HuffmanNode)
          and self.val == other.val
          and self.occ == other.occ
        )

    def __repr__(self):
        return ("HuffmanNode({!r}, {!r})".format(self.val, self.occ))

# HuffmanTree HuffmanTree -> bool
# returns true if tree a comes before tree b
def comes_before(a, b):
   if b == None or a > b:
      return True
   elif a == None or b > a:
      return False

# string -> list
# reads from a given file and counts frequency of occurences of all chars in file
def read_file(file_name):
   file = open(file_name)
   chars_list = ArrayList([0]*256, 256)
   for line in file:
      for ch in line:
         chars_list.array[ord(ch)] += 1
   file.close()
   return chars_list

# HuffmanTree -> str
# uses a pre-order traversal through the given Huffman Tree to create a string
def preorder(hTree):
   if hTree == None:
      return None
   else
      return Pair(hTree.value, append(preorder(hTree.left), preorder(hTree.right)))

# str -> 
