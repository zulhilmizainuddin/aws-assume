import os
import unittest

from fixture.response import assumed_role_response

from credentials_cache import CredentialsCache
from data_models import AssumeRoleArgs, AssumedRoleUser, Credentials, AssumedRoleResponse


class TestCredentialsCache(unittest.TestCase):

    def setUp(self):
        self.credentials_cache = CredentialsCache()

        self.assume_role_args = AssumeRoleArgs(role_arn='arn:aws:iam::123456789012:role/rolename', role_session_name='sessionname')

        self.assumed_role_user = AssumedRoleUser(assumed_role_id=assumed_role_response['AssumedRoleUser']['AssumedRoleId'],
                                                 arn=assumed_role_response['AssumedRoleUser']['Arn'])

        self.credentials = Credentials(access_key_id=assumed_role_response['Credentials']['AccessKeyId'],
                                       secret_access_key=assumed_role_response['Credentials']['SecretAccessKey'],
                                       session_token=assumed_role_response['Credentials']['SessionToken'],
                                       expiration=assumed_role_response['Credentials']['Expiration'])

        self.assumed_role_response = AssumedRoleResponse(assumed_role_user=self.assumed_role_user,
                                                         credentials=self.credentials)

    def test_cache_directory_name(self):
        self.assertEqual(self.credentials_cache.cache_directory,
                         f'{os.path.expanduser("~")}/.awsassume/cache')

    def test_cache_directory_exist(self):
        self.assertTrue(os.path.exists(self.credentials_cache.cache_directory))

    def test_get_cache_name(self):
        self.assertEqual(self.credentials_cache.get_cache_name(self.assume_role_args),
                         'sessionname__123456789012_rolename')

    def test_get_cache_full_path(self):
        self.assertEqual(self.credentials_cache.get_cache_full_path(self.assume_role_args),
                         f'{self.credentials_cache.cache_directory}/sessionname__123456789012_rolename')

    def test_set_get_delete_aws_credentials(self):
        self.credentials_cache.set_aws_credentials_to_cache(self.assume_role_args, self.assumed_role_response)
        self.assertTrue(os.path.isfile(f'{self.credentials_cache.cache_directory}/sessionname__123456789012_rolename'))

        cached_assumed_role_response = self.credentials_cache.get_aws_credentials_from_cache(self.assume_role_args)
        self.assertEqual(cached_assumed_role_response, self.assumed_role_response)

        self.credentials_cache.delete_cache_file(self.assume_role_args)
        self.assertFalse(os.path.isfile(f'{self.credentials_cache.cache_directory}/sessionname__123456789012_rolename'))


if __name__ == '__main__':
    unittest.main()
