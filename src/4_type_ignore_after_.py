from uuid import UUID

class AppClient: ...
client = AppClient()
def get_name(user_id: UUID) -> str: ...
client.name = get_name(  # type: ignore[attr-defined]
    UUID("123e4567-e89b-12d3-a456-426614174000")
)
