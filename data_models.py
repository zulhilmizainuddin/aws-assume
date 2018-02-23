from collections import namedtuple


AssumeRoleArgs = namedtuple('AssumeRoleArgs', 'role_arn role_session_name')

AWSAssumedRoleUser = namedtuple('AWSAssumedRoleUser', 'assumed_role_id arn')
AWSCredentials = namedtuple('AWSCredentials', 'access_key_id secret_access_key session_token expiration')
AWSAssumedRoleResponse = namedtuple('AWSAssumedRoleResponse', 'assumed_role_user credentials')
