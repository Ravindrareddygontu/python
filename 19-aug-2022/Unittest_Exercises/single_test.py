##import unittest
##
##class Test(unittest.TestCase):
##    def test_case1(self):
##        a = 9
##        b = 8
##        c = a+b
##        self.assertEqual(c,17)
##        
##unittest.main()

import re
s = 'Twelve:12 Eighty nine:89'
pa = '\d+'

r = re.split(pa,s)
print(r)
