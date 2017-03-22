import unittest

class PaloAPIServerTestSuper(unittest.TestCase):
	def setUp(self):
		print("setUp PaloAPIServerTest")
		
	def tearDown(self):
		print("tearDown PaloAPIServerTest")

		
class PaloAPIServerTest(PaloAPIServerTestSuper):
	def runTest(self):
		print("Running PaloAPIServerTest")
		
	@unittest.skip("not yet implemented ...")
    def test_activate_license(self):
		""" Test addition and fail. """
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_change_password(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_databases(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_info(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_licenses(self):
        self.assertEqual(1, 1)
		
	@unittest.skip("not yet implemented ...")
	def test_load(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_login(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_logout(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_save(self):
        self.assertEqual(1, 1)
	
	@unittest.skip("not yet implemented ...")
	def test_shutdown(self):
        self.assertEqual(1, 1)
		
	@unittest.skip("not yet implemented ...")
	def test_user_info(self):
        self.assertEqual(1, 1)
		
	
def suite():
    suite = unittest.TestSuite()
	
    # Variante I
	suite.addTest(PaloAPIServerTest())
	
	# Variante II
	suite.addTest(PaloAPIServerTest('test_info'))
    suite.addTest(PaloAPIServerTest('test_login'))
    suite.addTest(PaloAPIServerTest('test_logout'))
	
    return suite
	
	
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
