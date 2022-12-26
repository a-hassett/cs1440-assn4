import unittest

# from Testing import Test
import Test


suite = unittest.TestSuite()  	         	  
tests = Test.Test
suite.addTest(unittest.makeSuite(tests))

runner = unittest.TextTestRunner(verbosity=2)  	         	  
runner.run(suite)  	         	  
