import os
import pytest

from awsassume.data_models import AssumeRoleType, ResponseCacheArgs
from awsassume.response_cache_adapter import ResponseCacheAdapter


@pytest.fixture(scope='module', autouse=True)
def response_cache_adapter(response_cache_args):
    return ResponseCacheAdapter(response_cache_args)


@pytest.fixture(scope='module')
def response_cache_args():
    return ResponseCacheArgs('arn:aws:iam::123456789012:role/rolename',
                             'sessionname',
                             'ap-southeast-1',
                             AssumeRoleType.DEFAULT)


@pytest.fixture(scope='module')
def assumed_role_response():
    from fixture.assumed_role_response import assumed_role_response

    return assumed_role_response


def test_set_get_delete_response(response_cache_adapter, assumed_role_response):
    cache_directory = response_cache_adapter.response_cache.cache_directory

    response_cache_adapter.set_response_to_cache(assumed_role_response)
    assert os.path.isfile(f'{cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT') is True

    cached_assumed_role_response = response_cache_adapter.get_response_from_cache()
    assert cached_assumed_role_response == assumed_role_response

    response_cache_adapter.delete_cache_file()
    assert os.path.isfile(f'{cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT') is False
