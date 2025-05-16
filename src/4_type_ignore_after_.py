import uuid
from uuid import UUID

class AppClient: ...
client = AppClient()
user_id: uuid.UUID =  UUID("123e4567-e89b-12d3-a456-426614174000")
def get_name(user_id: UUID) -> str: ...
client.name = get_name(user_id)  # type: ignore[attr-defined]

