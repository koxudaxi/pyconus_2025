# runs on 3.9+
from typing_extensions import TypeIs

def is_str(x: object) -> TypeIs[str]:
    return isinstance(x, str)