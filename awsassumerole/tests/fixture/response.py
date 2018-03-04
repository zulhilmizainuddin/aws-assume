import datetime


def tzutc():
    return None


def tzlocal():
    return None


assume_role_response = {
    'ResponseMetadata': {
        'RetryAttempts': 0,
        'HTTPHeaders': {
            'content-type': 'text/xml',
            'x-amzn-requestid': 'fb44fd81-1738-11e8-91fd-251c48d5b45c',
            'date': 'Wed, 21 Feb 2018 18:56:53 GMT',
            'content-length': '1051'
        },
        'HTTPStatusCode': 200,
        'RequestId': 'fb44fd81-1738-11e8-91fd-251c48d5b45c'
    },
    'AssumedRoleUser': {
        'AssumedRoleId': 'AROAJDZWOM3D72FCH3NLI:role-session-name',
        'Arn': 'arn:aws:sts::123456789012:assumed-role/role-name/role-session-name'
    },
    'Credentials': {
        'AccessKeyId': 'ASIAJJVQX43FAN6HSXDQ',
        'Expiration': datetime.datetime(2018,
                                       2,
                                       21,
                                       19,
                                       56,
                                       53,
                                       tzinfo=tzutc()),
        'SessionToken': 'FQoDYXdzEDQaDKW/lVgwUTPADHdnxiLqAWXK4Rb5hihPSj+vIp3TRdHZdlzTlYEmeHUrqhjbKtk/JlFjEDzj8HVbxgLUZZDsJaE5Q46N4vUowl+qq4Pok58DfxvWG3lOJmxb2KO+XezUj6WWCYPUI2PHQ7/VeVJqs7tM6CNgimNUuFx2I9X32vVuWWpo7VPGD5rbx6Ikqf1SOJeyghgHGR4pYg1uVA64x3qRQ4PkUbGN8tB/k8USX3urWwSs1JX1oR6VslPNxy6XR3d4R0rkwyXWHou+e4wHW4+7MlretfWtH0vM+UaV3hRH+BKu9/y+nmRNg14HnOFdO6179MvNx26Upyj1gbfUBQ==',
        'SecretAccessKey': 'rJWZn5j2KkjKGU/2xH6p2JE8oY85+7heKKZhPBWg'
    }
}
