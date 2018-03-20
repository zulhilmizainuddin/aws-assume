from argparse import Namespace
from datetime import datetime
from typing import Any, Dict, NamedTuple


class AssumeRoleArgs(NamedTuple):
    role_arn: str
    role_session_name: str
    region_name: str


AssumedRoleResponse = Dict[str, Any]


AssumedRoleResponseCredentials = Dict[str, Any]


CliArgs = Namespace


class Credentials(NamedTuple):
    access_key_id: str
    secret_access_key: str
    session_token: str
    expiration: datetime
