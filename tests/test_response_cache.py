import os
import pytest

from data_models import AssumeRoleType, ResponseCacheArgs
from response_cache import ResponseCache


@pytest.fixture(scope='module', autouse=True)
def response_cache():
    return ResponseCache()


@pytest.fixture(scope='module')
def response_cache_args():
    return ResponseCacheArgs('arn:aws:iam::123456789012:role/rolename',
                             'sessionname',
                             'ap-southeast-1',
                             AssumeRoleType.DEFAULT)


@pytest.fixture(scope='module')
def cache_directory():
    return f'{os.path.expanduser("~")}/.awsassume/cache'


@pytest.fixture(scope='module')
def assumed_role_response():
    from fixture.assumed_role_response import assumed_role_response

    return assumed_role_response


def test_cache_directory_name(cache_directory):
    assert cache_directory == f'{os.path.expanduser("~")}/.awsassume/cache'


def test_cache_directory_exist(cache_directory):
    assert os.path.exists(cache_directory) is True


def test_get_cache_name(response_cache, response_cache_args):
    cache_name = response_cache.get_cache_name(response_cache_args)

    assert cache_name == 'sessionname__123456789012_rolename__ap-southeast-1__DEFAULT'


def test_get_cache_full_path(response_cache, response_cache_args, cache_directory):
    cache_full_path = response_cache.get_cache_full_path(response_cache_args)

    assert cache_full_path == f'{cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT'


def test_set_get_delete_response(response_cache, response_cache_args, cache_directory, assumed_role_response):
    response_cache.set_response_to_cache(response_cache_args, assumed_role_response)
    assert os.path.isfile(f'{cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT') is True

    cached_assumed_role_response = response_cache.get_response_from_cache(response_cache_args)
    assert cached_assumed_role_response == assumed_role_response

    response_cache.delete_cache_file(response_cache_args)
    assert os.path.isfile(f'{cache_directory}/sessionname__123456789012_rolename__ap-southeast-1__DEFAULT') is False
