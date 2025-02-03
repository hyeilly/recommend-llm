from fastapi import FastAPI, APIRouter
from core_api.app.services.test import TestPrinter

app = FastAPI(title="recommend-llm", description="LLM 추천 프로젝트 API 서비스")
router = APIRouter()

app.include_router(router)
@router.get("/")
async def root():
    return {"message": "Welcome to recommend-llm API"}

@router.get("/zxc0585")
async def example():
    return {"message": "This is the example endpoint zxc0585"}

# @app.get("/")
# async def root():
#     printer = TestPrinter()
#     printer.print_test()
#     return {"message": "Welcome to recommend-llm API123123"}
#
# @app.get("/zxc0585")
# async def example():
#     return {"message": "This is the example endpoint zxc0585"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)
