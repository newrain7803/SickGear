# Stubs for tornado_py3.wsgi (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tornado_py3 import httputil
from typing import Any, Dict, Text
from wsgiref.types import WSGIApplication as WSGIAppType

def to_wsgi_str(s: bytes) -> str: ...

class WSGIContainer:
    wsgi_application: Any = ...
    def __init__(self, wsgi_application: WSGIAppType) -> None: ...
    def __call__(self, request: httputil.HTTPServerRequest) -> None: ...
    @staticmethod
    def environ(request: httputil.HTTPServerRequest) -> Dict[Text, Any]: ...
HTTPRequest = httputil.HTTPServerRequest