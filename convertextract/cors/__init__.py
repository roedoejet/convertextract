"""
Route the request to the appropriate correspondence list based on cli argument.
"""

import os
import re
import importlib
from .. import exceptions
from .correspondences import Correspondence


DEFAULT_ENCODING = 'utf_8'


def processCors(language):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    if not isinstance(language, type(None)):
        if not re.search(r'\.xlsx', language):
            if not os.path.exists(os.path.join(this_dir, "correspondence_spreadsheets", language + '.xlsx')):
                raise exceptions.CorrespondenceMissing(language)
    cor = Correspondence(language)
    return cor