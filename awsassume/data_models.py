from datetime import datetime
from typing import NamedTuple


class AssumeRoleArgs(NamedTuple):
    role_arn: str
    role_session_name: str


class Credentials(NamedTuple):
    access_key_id: str
    secret_access_key: str
    session_token: str
    expiration: datetime
