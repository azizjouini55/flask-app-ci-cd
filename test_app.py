import unittest
from app import app

class TestHello(unittest.TestCase):
    def test_hello(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.data, b'halo, World!')

if __name__ == '__main__':
    unittest.main()

