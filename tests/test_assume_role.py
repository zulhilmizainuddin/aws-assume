import pytest

from unittest.mock import MagicMock

from awsassume.assume_role import AssumeRole
from awsassume.data_models import AssumeRoleArgs


@pytest.fixture(scope='module')
def assume_role():
    assume_role_args = AssumeRoleArgs(role_arn='arn:aws:iam::123456789012:role/rolename',
                                      role_session_name='sessionname')

    return AssumeRole(assume_role_args)


@pytest.fixture(scope='module')
def assumed_role_response():
    from fixture.assumed_role_response import assumed_role_response

    return assumed_role_response


def test_assume_role(assume_role, assumed_role_response):
    assume_role.client.assume_role = MagicMock(return_value=assumed_role_response)

    assert assume_role.assume_role() == assumed_role_response
