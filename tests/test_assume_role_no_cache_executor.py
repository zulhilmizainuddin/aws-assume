import datetime
import pytest

from assume_role import AssumeRole
from assume_role_no_cache_executor import AssumeRoleNoCacheExecutor
from data_models import AssumeRoleArgs, Credentials
from dateutil.tz import tzutc
from unittest.mock import MagicMock


@pytest.fixture(scope='module')
def assume_role():
    assume_role_args = AssumeRoleArgs(role_arn='arn:aws:iam::123456789012:role/rolename',
                                      role_session_name='sessionname')

    return AssumeRole(assume_role_args)


@pytest.fixture(scope='module')
def assume_role_no_cache_executor(assume_role):
    return AssumeRoleNoCacheExecutor(assume_role)


@pytest.fixture(scope='module')
def assumed_role_response():
    from fixture.assumed_role_response import assumed_role_response

    return assumed_role_response


@pytest.fixture(scope='module')
def credentials():
    return Credentials(access_key_id='ASIAJJVQX43FAN6HSXDQ',
                       secret_access_key='rJWZn5j2KkjKGU/2xH6p2JE8oY85+7heKKZhPBWg',
                       session_token='FQoDYXdzEDQaDKW/lVgwUTPADHdnxiLqAWXK4Rb5hihPSj+vIp3TRdHZdlzTlYEmeHUrqhjbKtk/JlFjEDzj8HVbxgLUZZDsJaE5Q46N4vUowl+qq4Pok58DfxvWG3lOJmxb2KO+XezUj6WWCYPUI2PHQ7/VeVJqs7tM6CNgimNUuFx2I9X32vVuWWpo7VPGD5rbx6Ikqf1SOJeyghgHGR4pYg1uVA64x3qRQ4PkUbGN8tB/k8USX3urWwSs1JX1oR6VslPNxy6XR3d4R0rkwyXWHou+e4wHW4+7MlretfWtH0vM+UaV3hRH+BKu9/y+nmRNg14HnOFdO6179MvNx26Upyj1gbfUBQ==',
                       expiration=datetime.datetime(2018, 2, 21, 19, 56, 53, tzinfo=tzutc()))


def test_execute(assume_role_no_cache_executor, assumed_role_response, credentials):
    assume_role_no_cache_executor.security_token_service.assume_role = MagicMock(return_value=assumed_role_response)

    assert assume_role_no_cache_executor.execute() == credentials
