import unittest
import sys
import os

try:
    from flounder.flounder import Flounder
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from flounder.flounder import Flounder

CLIENT_ACCESS_TOKEN = '704feeb63be04870ab69b9de12ca1331'


class TestActions(unittest.TestCase):
    def setUp(self):
        self.flounder = Flounder(CLIENT_ACCESS_TOKEN)

    def test_create_entity(self):
        create_request = self.flounder.create_request()
        response = create_request.getresponse()
        print response.status, response.reason
        return response


if __name__ == '__main__':
    unittest.main()