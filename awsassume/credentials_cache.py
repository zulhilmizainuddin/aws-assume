import errno
import os
import pickle
import re

from data_models import AssumeRoleArgs
from typing import Any, Dict


class CredentialsCache(object):
    cache_directory = f'{os.path.expanduser("~")}/.awsassume/cache'

    def __init__(self) -> None:
        try:
            os.makedirs(CredentialsCache.cache_directory)
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

    def set_aws_credentials_to_cache(self, assume_role_args: AssumeRoleArgs, assumed_role_response: Dict[str, Any]) -> None:
        try:
            with open(self.get_cache_full_path(assume_role_args), 'wb') as file:
                pickle.dump(assumed_role_response, file)
        except OSError:
            raise

    def get_aws_credentials_from_cache(self, assume_role_args: AssumeRoleArgs) -> Dict[str, Any]:
        assumed_role_response: Dict[str, Any] = None

        try:
            with open(self.get_cache_full_path(assume_role_args), 'rb') as file:
                assumed_role_response = pickle.load(file)
        except OSError:
            raise

        return assumed_role_response

    def delete_cache_file(self, assume_role_args: AssumeRoleArgs) -> None:
        try:
            os.remove(self.get_cache_full_path(assume_role_args))
        except OSError:
            raise

    def get_cache_full_path(self, assume_role_args: AssumeRoleArgs) -> str:
        full_path = f'{CredentialsCache.cache_directory}/{self.get_cache_name(assume_role_args)}'

        return full_path

    def get_cache_name(self, assume_role_args: AssumeRoleArgs) -> str:
        cache_name: str = None

        matched_arn = re.match('arn:aws:iam::([0-9]{12}):role/([0-9a-zA-Z+=,.@\-_]{1,64})', assume_role_args.role_arn)
        if matched_arn:
            role_session_name_section = assume_role_args.role_session_name
            role_arn_section = f'{matched_arn.group(1)}_{matched_arn.group(2)}'

            cache_name = f'{role_session_name_section}__{role_arn_section}'

        return cache_name
