from fastapi import APIRouter
router=APIRouter(tags=["Health"])

@router.get("/health-check")

async def health_check()->dict [str,str]:
    return {"Status":"OK"}