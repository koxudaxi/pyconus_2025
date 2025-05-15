from typing import TypeGuard

def is_int(x: str | int) -> TypeGuard[int]:
    return isinstance(x, int)

def use(x: str | int) -> str | int:
    if is_int(x):
        return x + 1      # ✅ int
    else:
        return x.upper()  # ⚠️ may still be int

