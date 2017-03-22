import unittest

class PaloAPIServerTestSuper(unittest.TestCase):
	def setUp(self):
		print("setUp PaloAPIServerTest")
		
	def tearDown(self):
		print("tearDown PaloAPIServerTest")

		
class PaloAPIServerTest(PaloAPIServerTestSuper):
		
	@unittest.skip("not yet implemented ...")
    def runTestActivateLicense(self):
		""" Test addition and fail. """
		print("Running runTestActivateLicense")
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestChangePassword(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestDatabases(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestInfo(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestLicenses(self):
        self.assertEqual(1, 1)
		
	@unittest.skip("not yet implemented ...")
	def runTestLoad(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestLogin(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestLogout(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestSave(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def runTestShutdown(self):
        self.assertEqual(1, 1)
		
	@unittest.skip("not yet implemented ...")
	def runTestUserInfo(self):
        self.assertEqual(1, 1)
		
	
def suite():
    suite = unittest.TestSuite()
	
    # Variante I
	suite.addTest(PaloAPIServerTest())
	
	# Variante II
	suite.addTest(PaloAPIServerTest('runTestInfo'))
    suite.addTest(PaloAPIServerTest('runTestLogin'))
    suite.addTest(PaloAPIServerTest('runTestLogout'))
	
    return suite
	
	
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
