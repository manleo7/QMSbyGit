from fastapi import FastAPI
from app.api import quality_issue, auth, ai, files, ws

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(quality_issue.router, prefix="/quality-issues")
app.include_router(ai.router, prefix="/ai")
app.include_router(files.router, prefix="/files")
app.include_router(ws.router)