from DS.list import Single_Linked_List
import unittest


class ListTest(unittest.TestCase):

    def test_list(self):
        l1 = Single_Linked_List()
        self.assertFalse(l1.remove(1))

l1 = Single_Linked_List()
l1.printall()
for i in range(10):
    l1.insert(i)

l1.printall()

l1.remove(0)
l1.printall()
l1.remove(9)
l1.printall()
l1.remove(5)
l1.printall()
