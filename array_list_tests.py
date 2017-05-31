import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def testCreation0(self):
        self.assertEqual(ArrayList([3, 4, 5, None, None], 5), ArrayList([3, 4, 5, None, None], 5))

    def test_make_empty(self):
        self.assertEqual(make_empty(), ArrayList([None, None, None, None, None], 0))

    def test_length(self):
        self.assertEqual(length(ArrayList([2, 55, None, None], 2)), 2)

    def test_length2(self):
        self.assertEqual(length(ArrayList([66, 9, None, None], 3)), 3)

    def test_add_to_end(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertEqual(add_to_end(obj, "word"), obj)
        self.assertEqual(obj, ArrayList([2, 10, "word", None], 3))

    def test_add_to_end2(self):
        obj = ArrayList([2, 10], 2)
        self.assertEqual(add_to_end(obj, "word"), obj)
        self.assertEqual(obj, ArrayList([2, 10, "word", None], 3))

   def test_add(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertEqual(add(obj, 2, "word"), obj)
        self.assertEqual(obj, ArrayList([2, 10, "word", None], 3))

    def test_add2(self):
        obj = ArrayList([2, 10], 2)
        self.assertEqual(add(obj, 2, "word"), obj)
        self.assertEqual(obj, ArrayList([2, 10, "word", None], 3))

    def test_add3(self):
        obj = ArrayList([2, 10], 2)
        self.assertEqual(add(obj, 0, "word"), obj)
        self.assertEqual(obj, ArrayList(["word", 2, 10, None], 3))

    def test_get(self):
        self.assertEqual(get(ArrayList([2, 10, None, None], 2), 0), 2)

    def test_get2(self):
        self.assertEqual(get(ArrayList([2, 10, None, None], 2), 1), 10)

    def test_get3(self):
        self.assertRaises(IndexError, get, ArrayList([2, 10, None, None], 2), 9)

    def test_get4(self):
        self.assertRaises(IndexError, get, ArrayList([9, 10, None, None], 2), -1)

    def test_set(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertEqual(set(obj, 0, "word"), obj)
        self.assertEqual(obj, ArrayList(["word", 10, None, None], 2))

    def test_set2(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertEqual(set(obj, 1, "word"), obj)
        self.assertEqual(obj, ArrayList([2, "word", None, None], 2))

   def test_set3(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertRaises(IndexError, set, obj, 2, "word")

    def test_remove(self):
        obj = ArrayList([9, 10, None, None], 2)
        self.assertEqual(remove(obj, 0), obj)
        self.assertEqual(obj, ArrayList([10, None, None, None], 1))

    def test_remove2(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertEqual(remove(obj, 1), obj)
        self.assertEqual(obj, ArrayList([2, None, None, None], 1))

    def test_remove3(self):
        obj = ArrayList([2, 10, None, None], 2)
        self.assertRaises(IndexError, remove, obj, 2)

if __name__ == '__main__':
    unittest.main()

