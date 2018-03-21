from datetime import datetime
from typing import Any, Dict, List, NamedTuple


class AssumeRoleArgs(NamedTuple):
    role_arn: str
    role_session_name: str
    region_name: str


AssumedRoleResponse = Dict[str, Any]


AssumedRoleResponseCredentials = Dict[str, Any]


class CliArgs(NamedTuple):
    role_arn: str
    role_session_name: str
    command: List[str]
    no_cache: bool
    region_name: str


class Credentials(NamedTuple):
    access_key_id: str
    secret_access_key: str
    session_token: str
    expiration: datetime
