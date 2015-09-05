import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.val = 0
        #print self.val
        self.val += 1
        #print self.val

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("FoO".isupper())
        
    def runTest(self):
        print "runtest"
        self.assertEqual(1 in [1, 2], True)

if __name__=='__main__':
    unittest.main()

#tc1 = TestStringMethods('test_upper')
#result = unittest.TestResult()

#def suite():
    #suite = unittest.TestSuite()
    #suite.addTest(tc1)
    #return suite

#print suite().run(result)