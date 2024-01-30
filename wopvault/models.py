from typing import List, Tuple

from pydantic import BaseModel


class Drawing(BaseModel):
    curves: List[List[Tuple[float, float]]]
