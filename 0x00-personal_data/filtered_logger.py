#!/usr/bin/env python3
"""
    Regexing
"""


import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, seperator: str,
        ) -> str:
    """
    Filters a log line
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, seperator), replace(redaction), message)
