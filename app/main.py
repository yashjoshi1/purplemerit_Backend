from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, users

app = FastAPI(title="PurpleMerit Backend API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://purplemerit-frontend.vercel.app",
        "https://purplemerit-frontend-jhvsudojw-yashjoshis-projects.vercel.app",
        "https://purplemerit-frontend.vercel.app/"
        "https://purplemerit-frontend.vercel.app/login"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(users.router)


@app.middleware("http")
async def log_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        raise

@app.get("/")
def root():
    return {"message": "Backend is running"}
