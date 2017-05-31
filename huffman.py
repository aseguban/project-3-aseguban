from array_list import *

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
