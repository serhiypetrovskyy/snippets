import unittest


class TestSomeClassA(unittest.TestCase):

    def setUp(self):
        pass
        # Will run before every test to set up required prerequisites

    def test_some_test_caseA(self):
        pass

    def test_some_test_caseB(self):
        pass

    def tearDown(self):
        pass
        # Will run after every test to clean up what was set up


# Class level setup and teardown example


class TestSomeClassB(unittest.TestCase):

    def setUpClass(cls):
        pass
        # Will run once before ALL tests

    def test_some_test_caseA(self):
        pass

    def test_some_test_caseB(self):
        pass

    def tearDownClass(cls):
        pass
        # Will run once after ALL tests


if __name__ == "__main__":
    unittest.main(verbosity=2)
