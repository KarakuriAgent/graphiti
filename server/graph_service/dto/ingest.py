from datetime import datetime
from pydantic import BaseModel, Field

from graph_service.dto.common import Message
from graphiti_core.utils.datetime_utils import utc_now


class AddMessagesRequest(BaseModel):
    group_id: str = Field(..., description='The group id of the messages to add')
    messages: list[Message] = Field(..., description='The messages to add')


class AddTextRequest(BaseModel):
    group_id: str = Field(..., description='The group id of the text to add')
    content: str = Field(..., description='The text content to add')
    uuid: str | None = Field(default=None, description='The uuid of the text episode (optional)')
    name: str = Field(default='', description='The name of the episodic node for the text (optional)')
    reference_time: datetime = Field(default_factory=utc_now, description='The timestamp of the text')
    source_description: str = Field(default='', description='The description of the source of the text')


class AddEntityNodeRequest(BaseModel):
    uuid: str = Field(..., description='The uuid of the node to add')
    group_id: str = Field(..., description='The group id of the node to add')
    name: str = Field(..., description='The name of the node to add')
    summary: str = Field(default='', description='The summary of the node to add')
