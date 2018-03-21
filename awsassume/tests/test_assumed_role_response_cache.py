import os
import unittest

from fixture.assumed_role_response import assumed_role_response

from assumed_role_response_cache import AssumedRoleResponseCache


class TestAssumedRoleResponseCache(unittest.TestCase):

    def setUp(self):
        self.response_cache = AssumedRoleResponseCache('arn:aws:iam::123456789012:role/rolename', 'sessionname', 'ap-southeast-1')

        self.assumed_role_response = assumed_role_response

    def test_cache_directory_name(self):
        self.assertEqual(self.response_cache.cache_directory,
                         f'{os.path.expanduser("~")}/.awsassume/cache')

    def test_cache_directory_exist(self):
        self.assertTrue(os.path.exists(self.response_cache.cache_directory))

    def test_get_cache_name(self):
        self.assertEqual(self.response_cache.get_cache_name(),
                         'sessionname__123456789012_rolename__ap-southeast-1')

    def test_get_cache_full_path(self):
        self.assertEqual(self.response_cache.get_cache_full_path(),
                         f'{self.response_cache.cache_directory}/sessionname__123456789012_rolename__ap-southeast-1')

    def test_set_get_delete_response(self):
        self.response_cache.set_response_to_cache(self.assumed_role_response)
        self.assertTrue(os.path.isfile(f'{self.response_cache.cache_directory}/sessionname__123456789012_rolename__ap-southeast-1'))

        cached_assumed_role_response = self.response_cache.get_response_from_cache()
        self.assertEqual(cached_assumed_role_response, self.assumed_role_response)

        self.response_cache.delete_cache_file()
        self.assertFalse(os.path.isfile(f'{self.response_cache.cache_directory}/sessionname__123456789012_rolename__ap-southeast-1'))


if __name__ == '__main__':
    unittest.main()
