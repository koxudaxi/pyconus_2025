from typing import TypedDict

class Item(TypedDict):
   id: int
   price: int

def total(items: list[Item]) -> int | float:
   ...   # some logic…

