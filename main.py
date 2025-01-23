from fastapi import FastAPI, APIRouter

router = APIRouter()

@app.get("/")
async def root():
    return {"message": "Welcome to recommend-llm API"}

@app.get("/zxc0585")
async def example():
    return {"message": "This is the example endpoint zxc0585"}


app = FastAPI(title="recommend-llm", description="LLM 추천 프로젝트 API 서비스")
app.include_router(router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)
