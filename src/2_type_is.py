from typing import TypeIs

def is_int(x: str | int) -> TypeIs[int]:
    return isinstance(x, int)

def use(x: str | int) -> str | int:
    if is_int(x):
        return x + 1      # ✅ int
    else:
        return x.upper()  # ✅ str