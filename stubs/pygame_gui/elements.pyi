from typing import Any, Tuple

from pygame import Rect

class UIButton:
    def __init__(self, relative_rect: Rect, text: str, manager: Any) -> None: ...

class UILabel:
    def __init__(self, relative_rect: Rect, text: str, manager: Any) -> None: ...
