from fastapi import FastAPI
from endpoints.test import router as service1_router

app = FastAPI()

app.include_router(service1_router, prefix="/test")

@app.get("/")
async def root():
    return {"message": "Welcome to service-repo-1 API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
