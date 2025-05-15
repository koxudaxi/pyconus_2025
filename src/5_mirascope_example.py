from mirascope import llm
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str

@llm.call(
    provider="openai",
    model="gpt-4o-mini",
    response_model=Book,
)
def extract_book(text: str) -> str:
    return f"Extract the book: {text}"

text = "The Name of the Wind by Patrick Rothfuss"
book: Book = extract_book(text)