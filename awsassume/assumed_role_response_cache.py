import errno
import os
import pickle
import re

from data_models import AssumedRoleResponse


class AssumedRoleResponseCache(object):
    cache_directory = f'{os.path.expanduser("~")}/.awsassume/cache'

    def __init__(self, role_arn: str, role_session_name: str, region_name: str = None) -> None:
        try:
            self.role_arn = role_arn
            self.role_session_name = role_session_name
            self.region_name = region_name

            os.makedirs(AssumedRoleResponseCache.cache_directory)
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

    def set_response_to_cache(self, assumed_role_response: AssumedRoleResponse) -> None:
        try:
            with open(self.get_cache_full_path(), 'wb') as file:
                pickle.dump(assumed_role_response, file)
        except OSError:
            raise

    def get_response_from_cache(self) -> AssumedRoleResponse:
        assumed_role_response: AssumedRoleResponse = None

        try:
            with open(self.get_cache_full_path(), 'rb') as file:
                assumed_role_response = pickle.load(file)
        except FileNotFoundError:
            pass
        except OSError:
            raise

        return assumed_role_response

    def delete_cache_file(self) -> None:
        try:
            os.remove(self.get_cache_full_path())
        except OSError:
            raise

    def get_cache_full_path(self) -> str:
        full_path = f'{AssumedRoleResponseCache.cache_directory}/{self.get_cache_name()}'

        return full_path

    def get_cache_name(self) -> str:
        cache_name: str = None

        matched_arn = re.match('arn:aws:iam::([0-9]{12}):role/([0-9a-zA-Z+=,.@\-_]{1,64})', self.role_arn)
        if matched_arn:
            role_session_name_section = self.role_session_name
            role_arn_section = f'{matched_arn.group(1)}_{matched_arn.group(2)}'

            region_name_section: str = 'default'
            if self.region_name is not None:
                region_name_section = self.region_name

            cache_name = f'{role_session_name_section}__{role_arn_section}__{region_name_section}'

        return cache_name
