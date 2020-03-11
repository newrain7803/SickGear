from ..util import FeedParserDict as FeedParserDict
from typing import Any

class Namespace:
    supported_namespaces: Any = ...
    ingeometry: int = ...
    def __init__(self) -> None: ...
    def _start_georssgeom(self, attrs_d: Any) -> None: ...
    _start_georss_point: Any = ...
    _start_georss_line: Any = ...
    _start_georss_polygon: Any = ...
    _start_georss_box: Any = ...
    def _save_where(self, geometry: Any) -> None: ...
    def _end_georss_point(self) -> None: ...
    def _end_georss_line(self) -> None: ...
    def _end_georss_polygon(self) -> None: ...
    def _end_georss_box(self) -> None: ...
    def _start_where(self, attrs_d: Any) -> None: ...
    _start_georss_where: Any = ...
    def _parse_srs_attrs(self, attrs_d: Any) -> None: ...
    def _start_gml_point(self, attrs_d: Any) -> None: ...
    def _start_gml_linestring(self, attrs_d: Any) -> None: ...
    def _start_gml_polygon(self, attrs_d: Any) -> None: ...
    def _start_gml_exterior(self, attrs_d: Any) -> None: ...
    def _start_gml_linearring(self, attrs_d: Any) -> None: ...
    def _start_gml_pos(self, attrs_d: Any) -> None: ...
    def _end_gml_pos(self) -> None: ...
    def _start_gml_poslist(self, attrs_d: Any) -> None: ...
    def _end_gml_poslist(self) -> None: ...
    def _end_geom(self) -> None: ...
    _end_gml_point: Any = ...
    _end_gml_linestring: Any = ...
    _end_gml_linearring: Any = ...
    _end_gml_exterior: Any = ...
    _end_gml_polygon: Any = ...
    def _end_where(self) -> None: ...
    _end_georss_where: Any = ...

def _parse_poslist(value: Any, geom_type: Any, swap: bool = ..., dims: int = ...): ...
def _gen_georss_coords(value: Any, swap: bool = ..., dims: int = ...) -> None: ...
def _parse_georss_point(value: Any, swap: bool = ..., dims: int = ...): ...
def _parse_georss_line(value: Any, swap: bool = ..., dims: int = ...): ...
def _parse_georss_polygon(value: Any, swap: bool = ..., dims: int = ...): ...
def _parse_georss_box(value: Any, swap: bool = ..., dims: int = ...): ...

_geogCS: Any
