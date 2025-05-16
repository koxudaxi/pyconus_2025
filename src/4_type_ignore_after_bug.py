from uuid import UUID

class AppClient: ...
client = AppClient()
def get_name(user_id: UUID) -> str: ...
client.name = get_name("123")  # type: ignore[attr-defined]

