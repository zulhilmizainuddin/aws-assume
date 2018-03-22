import os
import unittest

from fixture.assumed_role_response import assumed_role_response

from data_models import AssumeRoleType, ResponseCacheArgs
from response_cache import ResponseCache


class TestResponseCache(unittest.TestCase):

    def setUp(self):
        self.response_cache_args = ResponseCacheArgs('arn:aws:iam::123456789012:role/rolename',
                                                     'sessionname',
                                                     'ap-southeast-1',
                                                     AssumeRoleType.DEFAULT)

        self.response_cache = ResponseCache()

        self.assumed_role_response = assumed_role_response

    def test_cache_directory_name(self):
        self.assertEqual(self.response_cache.cache_directory,
                         f'{os.path.expanduser("~")}/.awsassume/cache')

    def test_cache_directory_exist(self):
        self.assertTrue(os.path.exists(self.response_cache.cache_directory))

    def test_get_cache_name(self):
        self.assertEqual(self.response_cache.get_cache_name(self.response_cache_args),
                         'sessionname__123456789012_rolename__ap-southeast-1__DEFAULT')

    def test_get_cache_full_path(self):
        self.assertEqual(self.response_cache.get_cache_full_path(self.response_cache_args),
                         f'{self.response_cache.cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT')

    def test_set_get_delete_response(self):
        self.response_cache.set_response_to_cache(self.response_cache_args, self.assumed_role_response)
        self.assertTrue(os.path.isfile(f'{self.response_cache.cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT'))

        cached_assumed_role_response = self.response_cache.get_response_from_cache(self.response_cache_args)
        self.assertEqual(cached_assumed_role_response, self.assumed_role_response)

        self.response_cache.delete_cache_file(self.response_cache_args)
        self.assertFalse(os.path.isfile(f'{self.response_cache.cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT'))


if __name__ == '__main__':
    unittest.main()
