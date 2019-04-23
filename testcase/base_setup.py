import unittest
from time import sleep
import ddt


class BaseSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()