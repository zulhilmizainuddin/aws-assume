from typing import NamedTuple


class AssumeRoleArgs(NamedTuple):
    role_arn: str
    role_session_name: str


class AssumedRoleUser(NamedTuple):
    assumed_role_id: str
    arn: str


class Credentials(NamedTuple):
    access_key_id: str
    secret_access_key: str
    session_token: str
    expiration: None


class AssumedRoleResponse(NamedTuple):
    assumed_role_user: AssumedRoleUser
    credentials: Credentials
