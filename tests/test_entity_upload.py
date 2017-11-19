import unittest
import sys
import os

try:
    from flounder.flounder import Flounder
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    from flounder.flounder import Flounder

DEVELOPER_ACCESS_TOKEN = ''

 
class TestFlounder(unittest.TestCase):
    def setUp(self):
        self.flounder = Flounder(DEVELOPER_ACCESS_TOKEN)
        return

    def test_create(self):
        create_request = self.flounder.create_request('Sushi', '/Users/flatfisher/Documents/git/dialogflow/flounder/tests/sushi.csv')
        response = create_request.getresponse()
        print response.read()
        print response.status, response.reason
        return


if __name__ == '__main__':
    unittest.main()