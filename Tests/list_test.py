from DS.list import Single_Linked_List
import unittest


class ListTest(unittest.TestCase):

    def test_list(self):
        test_remove = [3, 5, 7]
        l1 = Single_Linked_List()
        self.assertFalse(l1.remove(1))
        for i in range(10):
            l1.insert(i)
        self.assertListEqual(l1.to_array(), [i for i in range(10)])
        l1.remove(3)
        l1.remove(5)
        l1.remove(7)
        self.assertListEqual(l1.to_array(), [i for i in range(10) if i not in test_remove])
        for i in range(10):
            if i not in test_remove:
                l1.remove(i)
        self.assertListEqual(l1.to_array(), [])
        l1.insert(1)
        self.assertListEqual(l1.to_array(), [1])

    def test_init(self):
        l1 = Single_Linked_List()
        self.assertListEqual(l1.to_array(), [])

    def test_insert(self):
        l1 = Single_Linked_List()
        l1.insert(-1)
        self.assertListEqual(l1.to_array(), [-1])
