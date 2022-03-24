#! python3
import unittest
from l_list import Node, Linked_list, D_linked_list

class D_link_list_test(unittest.TestCase):
    '''Tests for doubly linked list'''

    def setUp(self):
        '''
        Create an empty list to work the tests with
        '''
        self.dlink_list = D_linked_list()
        self.dlink_list.insert('Test string data')
        self.dlink_list.insert('Test string data 02')

    def test_addElement(self):
        '''Add an element to the list'''
        self.assertEqual(len(self.dlink_list), 2)
        self.assertEqual(self.dlink_list.head.payload, 'Test string data 02')

    def test_search_index(self):
        self.assertEqual(self.dlink_list.search_index().index, 0)
        self.assertEqual(self.dlink_list.search_index(1).payload, 'Test string data 02')

    def test_del_element_00(self):
        '''Delete the node on key 0'''
        self.dlink_list.delete()
        self.assertEqual(len(self.dlink_list), 1)
        self.assertEqual(self.dlink_list.head.payload, 'Test string data 02')

    def test_del_element_01(self):
        '''Delete the node on key 1'''
        self.dlink_list.delete(1)
        self.assertEqual(len(self.dlink_list), 1)
        self.assertEqual(self.dlink_list.head.payload, 'Test string data')

    def test_traversing(self):
        for i in range(5):
            self.dlink_list.insert(f'dummy data {i}')
        contents = [node.payload for node in self.dlink_list.traverse()]
        print(contents, self.dlink_list.head.index)

if __name__ == '__main__':
    unittest.main()
