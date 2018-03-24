import datetime
import os
import pytest

from data_models import Credentials
from dateutil.tz import tzutc
from environment_variable import EnvironmentVariable


@pytest.fixture(scope='module')
def credentials():
    return Credentials(access_key_id='ASIAJJVQX43FAN6HSXDQ',
                       secret_access_key='rJWZn5j2KkjKGU/2xH6p2JE8oY85+7heKKZhPBWg',
                       session_token='FQoDYXdzEDQaDKW/lVgwUTPADHdnxiLqAWXK4Rb5hihPSj+vIp3TRdHZdlzTlYEmeHUrqhjbKtk/JlFjEDzj8HVbxgLUZZDsJaE5Q46N4vUowl+qq4Pok58DfxvWG3lOJmxb2KO+XezUj6WWCYPUI2PHQ7/VeVJqs7tM6CNgimNUuFx2I9X32vVuWWpo7VPGD5rbx6Ikqf1SOJeyghgHGR4pYg1uVA64x3qRQ4PkUbGN8tB/k8USX3urWwSs1JX1oR6VslPNxy6XR3d4R0rkwyXWHou+e4wHW4+7MlretfWtH0vM+UaV3hRH+BKu9/y+nmRNg14HnOFdO6179MvNx26Upyj1gbfUBQ==',
                       expiration=datetime.datetime(2018, 2, 21, 19, 56, 53, tzinfo=tzutc()))


@pytest.fixture(scope='module', params=[None, 'ap-southeast-1'])
def region_name(request):
    return request.param


def test_display_credentials_to_be_exported(credentials, region_name, capsys):
    EnvironmentVariable.display_credentials_to_be_exported(credentials, region_name)

    out, _ = capsys.readouterr()

    print_access_key_id = '# AWS_ACCESS_KEY_ID=ASIAJJVQX43FAN6HSXDQ'
    print_secret_access_key = '# AWS_SECRET_ACCESS_KEY=rJWZn5j2KkjKGU/2xH6p2JE8oY85+7heKKZhPBWg'
    print_session_token = '# AWS_SESSION_TOKEN=FQoDYXdzEDQaDKW/lVgwUTPADHdnxiLqAWXK4Rb5hihPSj+vIp3TRdHZdlzTlYEmeHUrqhjbKtk/JlFjEDzj8HVbxgLUZZDsJaE5Q46N4vUowl+qq4Pok58DfxvWG3lOJmxb2KO+XezUj6WWCYPUI2PHQ7/VeVJqs7tM6CNgimNUuFx2I9X32vVuWWpo7VPGD5rbx6Ikqf1SOJeyghgHGR4pYg1uVA64x3qRQ4PkUbGN8tB/k8USX3urWwSs1JX1oR6VslPNxy6XR3d4R0rkwyXWHou+e4wHW4+7MlretfWtH0vM+UaV3hRH+BKu9/y+nmRNg14HnOFdO6179MvNx26Upyj1gbfUBQ=='

    if region_name is not None:
        print_default_region = f'# AWS_DEFAULT_REGION={region_name}'

        assert out == f'{print_access_key_id}\n{print_secret_access_key}\n{print_session_token}\n{print_default_region}\n'
    else:
        assert out == f'{print_access_key_id}\n{print_secret_access_key}\n{print_session_token}\n'


def test_generate_command_to_export_credentials(credentials, region_name):
    exported_credentials = EnvironmentVariable.generate_command_to_export_credentials(credentials, region_name)

    export_access_key_id = f'export AWS_ACCESS_KEY_ID="ASIAJJVQX43FAN6HSXDQ"'
    export_secret_access_key = f'export AWS_SECRET_ACCESS_KEY="rJWZn5j2KkjKGU/2xH6p2JE8oY85+7heKKZhPBWg"'
    export_session_token = f'export AWS_SESSION_TOKEN="FQoDYXdzEDQaDKW/lVgwUTPADHdnxiLqAWXK4Rb5hihPSj+vIp3TRdHZdlzTlYEmeHUrqhjbKtk/JlFjEDzj8HVbxgLUZZDsJaE5Q46N4vUowl+qq4Pok58DfxvWG3lOJmxb2KO+XezUj6WWCYPUI2PHQ7/VeVJqs7tM6CNgimNUuFx2I9X32vVuWWpo7VPGD5rbx6Ikqf1SOJeyghgHGR4pYg1uVA64x3qRQ4PkUbGN8tB/k8USX3urWwSs1JX1oR6VslPNxy6XR3d4R0rkwyXWHou+e4wHW4+7MlretfWtH0vM+UaV3hRH+BKu9/y+nmRNg14HnOFdO6179MvNx26Upyj1gbfUBQ=="'

    if region_name is not None:
        export_default_region = f'export AWS_DEFAULT_REGION="{region_name}"'

        assert exported_credentials == f'{export_access_key_id}; {export_secret_access_key}; {export_session_token}; {export_default_region}'
    else:
        assert exported_credentials == f'{export_access_key_id}; {export_secret_access_key}; {export_session_token}'


def test_get_env_var_with_credentials(credentials, region_name):
    env_var_with_credentials = EnvironmentVariable.get_env_var_with_credentials(credentials, region_name)

    env_var_copy = os.environ.copy()

    env_var_copy['AWS_ACCESS_KEY_ID'] = 'ASIAJJVQX43FAN6HSXDQ'
    env_var_copy['AWS_SECRET_ACCESS_KEY'] = 'rJWZn5j2KkjKGU/2xH6p2JE8oY85+7heKKZhPBWg'
    env_var_copy['AWS_SESSION_TOKEN'] = 'FQoDYXdzEDQaDKW/lVgwUTPADHdnxiLqAWXK4Rb5hihPSj+vIp3TRdHZdlzTlYEmeHUrqhjbKtk/JlFjEDzj8HVbxgLUZZDsJaE5Q46N4vUowl+qq4Pok58DfxvWG3lOJmxb2KO+XezUj6WWCYPUI2PHQ7/VeVJqs7tM6CNgimNUuFx2I9X32vVuWWpo7VPGD5rbx6Ikqf1SOJeyghgHGR4pYg1uVA64x3qRQ4PkUbGN8tB/k8USX3urWwSs1JX1oR6VslPNxy6XR3d4R0rkwyXWHou+e4wHW4+7MlretfWtH0vM+UaV3hRH+BKu9/y+nmRNg14HnOFdO6179MvNx26Upyj1gbfUBQ=='

    if region_name is not None:
        env_var_copy['AWS_DEFAULT_REGION'] = region_name

    assert env_var_with_credentials == env_var_copy
