import os
import unittest

from fixture.assumed_role_response import assumed_role_response

from credentials_cache import CredentialsCache


class TestCredentialsCache(unittest.TestCase):

    def setUp(self):
        self.credentials_cache = CredentialsCache()

        self.role_arn = 'arn:aws:iam::123456789012:role/rolename'
        self.role_session_name = 'sessionname'

        self.assumed_role_response = assumed_role_response

    def test_cache_directory_name(self):
        self.assertEqual(self.credentials_cache.cache_directory,
                         f'{os.path.expanduser("~")}/.awsassume/cache')

    def test_cache_directory_exist(self):
        self.assertTrue(os.path.exists(self.credentials_cache.cache_directory))

    def test_get_cache_name(self):
        self.assertEqual(self.credentials_cache.get_cache_name(self.role_arn, self.role_session_name),
                         'sessionname__123456789012_rolename')

    def test_get_cache_full_path(self):
        self.assertEqual(self.credentials_cache.get_cache_full_path(self.role_arn, self.role_session_name),
                         f'{self.credentials_cache.cache_directory}/sessionname__123456789012_rolename')

    def test_set_get_delete_aws_credentials(self):
        self.credentials_cache.set_credentials_to_cache(self.role_arn, self.role_session_name, self.assumed_role_response)
        self.assertTrue(os.path.isfile(f'{self.credentials_cache.cache_directory}/sessionname__123456789012_rolename'))

        cached_assumed_role_response = self.credentials_cache.get_credentials_from_cache(self.role_arn, self.role_session_name)
        self.assertEqual(cached_assumed_role_response, self.assumed_role_response)

        self.credentials_cache.delete_cache_file(self.role_arn, self.role_session_name)
        self.assertFalse(os.path.isfile(f'{self.credentials_cache.cache_directory}/sessionname__123456789012_rolename'))


if __name__ == '__main__':
    unittest.main()
