from datetime import datetime
from pydantic import BaseModel, ConfigDict,Field

class SnippetCreate(BaseModel):
    model_config=ConfigDict(str_strip_whitespace=True)

    title: str|None=Field(
        default=None,
        max_length=100,
        example=["My Snippet Title"]
    )
    content: str=Field(
        min_length=1,
        max_length=10000,
        examples=["This is the content of my snippet."],
    )

class SnippetRead(BaseModel):
    code: str
    title: str|None
    content:str
    url: str
    created_at: datetime