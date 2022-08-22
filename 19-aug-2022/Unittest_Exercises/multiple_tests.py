import unittest

class st(unittest.TestCase):
    def test_case1(self):
        a = 9
        b = 8
        c = a+b
        self.assertEqual(c,17)

    def test_case2(self):
        lst = [3,4,6,3,5,9]
        self.assertIn(6,lst)
        self.assertNotIn(66,lst)

    def prime(self,num):
        for i in range(2,num):
            if num%i == 0:
                print('not prime')
        else:
            return 'prime'
    
    def test_case3(self):
        n = 7
        self.assertEqual(self.prime(n), 'prime')


unittest.main()