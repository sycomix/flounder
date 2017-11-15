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
        return

    def test_create(self):
        # entities = [
        #     Flounder.Entity(
        #         'dwarfs',
        #         [
        #             Flounder.Entry('Ori', ['ori', 'Nori']),
        #             Flounder.Entry('bifur', ['Bofur', 'Bombur']),
        #         ]
        #     )
        # ]
        # self.flounder.entities = entities
        create_request = self.flounder.create_request()
        print create_request.__dict__.keys()
        print create_request._connection.__dict__.keys()
        print create_request.base_url
        print create_request.create_parameters
        response = create_request.getresponse()
        print response.read()
        print response.status, response.reason
        return


if __name__ == '__main__':
    unittest.main()