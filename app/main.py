from fastapi import FastAPI
from app.api.email import router as email_router

app = FastAPI(
    title="IntelliMail API",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "service": "IntelliMail API",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }

app.include_router(email_router)