from .html import _BaseHTMLProcessor as _BaseHTMLProcessor
from .sgml import _SGML_AVAILABLE as _SGML_AVAILABLE
from .urls import make_safe_absolute_uri as make_safe_absolute_uri
from typing import Any, Optional

class _HTMLSanitizer(_BaseHTMLProcessor):
    acceptable_elements: Any = ...
    acceptable_attributes: Any = ...
    unacceptable_elements_with_end_tag: Any = ...
    acceptable_css_properties: Any = ...
    acceptable_css_keywords: Any = ...
    valid_css_values: Any = ...
    mathml_elements: Any = ...
    mathml_attributes: Any = ...
    svg_elements: Any = ...
    svg_attributes: Any = ...
    svg_attr_map: Any = ...
    svg_elem_map: Any = ...
    acceptable_svg_properties: Any = ...
    unacceptablestack: int = ...
    mathmlOK: int = ...
    svgOK: int = ...
    def __init__(self, encoding: Optional[Any] = ..., _type: str = ...) -> None: ...
    def reset(self) -> None: ...
    def unknown_starttag(self, tag: Any, attrs: Any) -> None: ...
    def unknown_endtag(self, tag: Any) -> None: ...
    def handle_pi(self, text: Any) -> None: ...
    def handle_decl(self, text: Any) -> None: ...
    def handle_data(self, text: Any) -> None: ...
    def sanitize_style(self, style: Any): ...
    def parse_comment(self, i: Any, report: int = ...): ...

def _sanitize_html(html_source: Any, encoding: Any, _type: Any): ...

RE_ENTITY_PATTERN: Any
RE_DOCTYPE_PATTERN: Any
RE_SAFE_ENTITY_PATTERN: Any

def replace_doctype(data: Any): ...
