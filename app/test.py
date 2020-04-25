import unittest
import server

class TestHello(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        rv = self.app.get('/add/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
TEST_CASES