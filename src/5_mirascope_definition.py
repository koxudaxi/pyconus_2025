from typing import TypedDict, NotRequired


class BaseCallParams(TypedDict, total=False): ...

class OpenAICallParams(BaseCallParams):
    temperature: NotRequired[float | None]