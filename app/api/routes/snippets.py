from fastapi import APIRouter

router=APIRouter(prefix="/snippets",tags=["Snippets"])

@router.get("")
async def list_snippets()->dict[str,str]:
    return {"message":"Snippets Router Working"}