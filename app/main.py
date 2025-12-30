from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI(title="PurpleMerit Backend API")

app.include_router(auth.router)
app.include_router(users.router)
from fastapi import Request

@app.middleware("http")
async def log_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print("🔥 ERROR:", e)
        raise
@app.get("/")
def root():
    return {"message": "Backend is running"}

