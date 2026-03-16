from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Scene:
    id: int
    title: str
    text: str
    choices: List[Tuple[str, int]]
    is_ending: bool