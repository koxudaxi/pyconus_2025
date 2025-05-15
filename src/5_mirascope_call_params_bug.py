from mirascope import llm

@llm.call(
    provider="openai",
    model="gpt-4o-mini",
    call_params={"temperature": "0.7"},   # ❌ str not float
)
def recommend_book(genre: str) -> str:
    return f"Recommend a {genre} book"


