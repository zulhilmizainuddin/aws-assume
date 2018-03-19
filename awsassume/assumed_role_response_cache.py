import errno
import os
import pickle
import re

from data_models import AssumedRoleResponse


class AssumedRoleResponseCache(object):
    cache_directory = f'{os.path.expanduser("~")}/.awsassume/cache'

    def __init__(self) -> None:
        try:
            os.makedirs(AssumedRoleResponseCache.cache_directory)
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

    def set_response_to_cache(self, role_arn: str, role_session_name: str, assumed_role_response: AssumedRoleResponse) -> None:
        try:
            with open(self.get_cache_full_path(role_arn, role_session_name), 'wb') as file:
                pickle.dump(assumed_role_response, file)
        except OSError:
            raise

    def get_response_from_cache(self, role_arn: str, role_session_name: str) -> AssumedRoleResponse:
        assumed_role_response: AssumedRoleResponse = None

        try:
            with open(self.get_cache_full_path(role_arn, role_session_name), 'rb') as file:
                assumed_role_response = pickle.load(file)
        except OSError:
            raise

        return assumed_role_response

    def delete_cache_file(self, role_arn: str, role_session_name: str) -> None:
        try:
            os.remove(self.get_cache_full_path(role_arn, role_session_name))
        except OSError:
            raise

    def get_cache_full_path(self, role_arn: str, role_session_name: str) -> str:
        full_path = f'{AssumedRoleResponseCache.cache_directory}/{self.get_cache_name(role_arn, role_session_name)}'

        return full_path

    def get_cache_name(self, role_arn: str, role_session_name: str) -> str:
        cache_name: str = None

        matched_arn = re.match('arn:aws:iam::([0-9]{12}):role/([0-9a-zA-Z+=,.@\-_]{1,64})', role_arn)
        if matched_arn:
            role_session_name_section = role_session_name
            role_arn_section = f'{matched_arn.group(1)}_{matched_arn.group(2)}'

            cache_name = f'{role_session_name_section}__{role_arn_section}'

        return cache_name
