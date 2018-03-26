import pytest

from assume_role_cache_executor import AssumeRoleCacheExecutor
from assume_role_executor_factory import AssumeRoleExecutorFactory
from assume_role_no_cache_executor import AssumeRoleNoCacheExecutor
from data_models import CliArgs


@pytest.fixture(scope='module', params=[True, False])
def cli_args(request):
    return CliArgs(role_arn='arn:aws:iam::123456789012:role/rolename',
                   role_session_name='sessionname',
                   command='aws s3 ls',
                   region_name='ap-southeast-1',
                   no_cache=request.param)


def test_get_executor(cli_args):
    assume_role_executor = AssumeRoleExecutorFactory.get_executor(cli_args)

    if cli_args.no_cache is True:
        assert isinstance(assume_role_executor, AssumeRoleNoCacheExecutor) is True
    else:
        assert isinstance(assume_role_executor, AssumeRoleCacheExecutor) is True
