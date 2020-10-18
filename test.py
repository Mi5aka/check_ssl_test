import unittest

from check_ssl import prepare_data, get_hosts, is_valid_hostname


class SslCheckTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_hosts(self):
        self.assertIsNotNone(get_hosts())

    def test_prepare_data(self):
        data = ['test.com', 'https://test.com/', 'test.com/1/1\n']
        result = list(map(prepare_data, data))
        self.assertEqual(result[0], 'test.com')
        self.assertEqual(result[1], 'test.com')
        self.assertEqual(result[2], 'test.com')

    def test_positive_is_valid_hostname(self):
        hostname = 'test.com'
        self.assertEqual(is_valid_hostname(hostname), True)

    def test_negative_is_valid_hostname(self):
        hostname = 'https://test.com/'
        self.assertEqual(is_valid_hostname(hostname), False)