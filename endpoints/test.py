from fastapi import APIRouter

router = APIRouter()

@router.get("/zxc0585", response_model=str)
async def check():
    return "test endpoint 연결 완료123123"
