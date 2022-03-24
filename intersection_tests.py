#! python3
# intersection.py tests to assert functionality
import unittest, random, time, datetime
import intersection

class arrayIntersectionTests(unittest.TestCase):
    ''' Tests for 'intersection.py' '''
    def setUp(self):
        ''' Create a random sample to test the functions. '''
        self.num_elems = 300_000
        self.arr_a = [random.randint(0,self.num_elems) for i in range(self.num_elems)]
        self.arr_b = [random.randint(0,self.num_elems) for i in range(self.num_elems)]
        #self.sample = list(set(self.arr_a).intersection(set(self.arr_b)))
    

    def test_same_elements(self):
        start = time.time()
        intersection.same_elements(self.arr_a, self.arr_b)
        elapsed = time.time() - start
        print(f'Took {str(datetime.timedelta(seconds=elapsed))} time to finish')

    
#     def test_intersection_dict(self):
#         start = time.time()
#         dict_from_list = {}
#         intersection = []
#         for element in self.arr_a:
#             dict_from_list[element] = None
#         elapsed = time.time() - start
#         print(f'Took {str(datetime.timedelta(seconds=elapsed))} time to finish')
#         # print(intersection)
'''
    def test_same_elements_alternative(self):
        self.assertEqual(intersection.same_elements_alternative(self.arr_a, self.arr_b), self.sample)

    def test_same_elements_with_sets(self):
        self.assertEqual(intersection.same_elements_with_sets(self.arr_a, self.arr_b), self.sample)

    def test_same_elements_with_comprehension(self):
        self.assertEqual(intersection.same_elements_with_comprehension(self.arr_a, self.arr_b), 
                                                                        self.sample)
'''
if __name__ == '__main__':
    unittest.main()
    