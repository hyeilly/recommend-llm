from fastapi import FastAPI, APIRouter

app = FastAPI(title="recommend-llm", description="LLM 추천 프로젝트 API 서비스")
router = APIRouter()

app.include_router(router)
@app.get("/")
async def root():
    return {"message": "Welcome to recommend-llm API"}

@app.get("/zxc0585")
async def example():
    return {"message": "This is the example endpoint zxc0585"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)
