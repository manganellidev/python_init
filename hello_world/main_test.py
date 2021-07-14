import main
import unittest

class MainTest(unittest.TestCase):
    def test_password_generation(self):
        self.assertTrue(main.gen_random_num())