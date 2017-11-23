import unittest


class ContinousTesting(unittest.TestCase):
    def setUp(self):
        print "some stuff"

    def test_search_in_python(self):
        print "some text"

if __name__ == "__main__":
    unittest.main