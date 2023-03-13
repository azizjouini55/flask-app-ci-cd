import unittest
from app import app

class TestHello(unittest.TestCase):
    def test_hello(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.data, b'halo, World!')
    def test_add_equipment(self):
        with app.test_client() as client:
            response = client.post('/equipment')
            self.assertEqual(response.data, b'<!doctype html>\n<html lang=en>\n<title>4[127 chars]p>\n')

if __name__ == '__main__':
    unittest.main()

