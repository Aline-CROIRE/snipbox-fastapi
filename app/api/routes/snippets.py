from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException,Request,status
from app.schemas.snippet import SnippetCreate, SnippetRead
from app.utils.codes import generate_code

router=APIRouter(prefix="/snippets",tags=["Snippets"])

_snippets :dict[str,dict]= {}

def _to_read(snippet: dict,request:Request)->SnippetRead:
    base_url=request.app.state.settings.base_url
    return SnippetRead(
        **snippet,
        url=f"{base_url}/snippets/{snippet['code']}",
    )

@router.post("",status_code=status.HTTP_201_CREATED)
async def create_snippet(payload: SnippetCreate, request: Request)->SnippetRead:
    code=generate_code()
    while code in _snippets:
        code=generate_code()

    snippet={
            "code": code,
            "title": payload.title,
            "content": payload.content,
            "created_at": datetime.now(timezone.utc),
        }
    _snippets[code]= snippet
    return _to_read(snippet,request)

@router.get("/{code}")
async def get_snippet(code: str, request: Request)->SnippetRead:
    snippet=_snippets.get(code)
    if snippet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="Snippet not found")
    return _to_read(snippet,request)