import uvicorn
from fastapi import FastAPI

from routers import summary_router

app = FastAPI()

app.include_router(summary_router.summary_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8800, reload=True)
