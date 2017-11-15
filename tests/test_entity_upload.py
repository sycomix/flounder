import unittest
import sys
import os

try:
    from flounder.flounder import Flounder
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from flounder.flounder import Flounder

CLIENT_ACCESS_TOKEN = 'CLIENT_ACCESS_TOKEN'


class TestActions(unittest.TestCase):
    def setUp(self):
        self.flounder = Flounder(CLIENT_ACCESS_TOKEN)

    def test_show_token(self):
        print self.flounder.client_access_token


if __name__ == '__main__':
    unittest.main()