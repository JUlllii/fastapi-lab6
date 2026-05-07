import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.init_dependencies import init_dependencies
from app.routes.config import router as config_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    deps = init_dependencies()
    app.state.deps = deps
    print("Зависимости инициализированы:", list(deps.keys()))
    yield
    print("Приложение остановлено.")


app = FastAPI(
    lifespan=lifespan,
    title=os.environ.get("APP_NAME", "Laboratory FastAPI App"),
    description=os.environ.get("APP_DESCRIPTION", "Учебное приложение на FastAPI"),
    version=os.environ.get("APP_VERSION", "1.0.0"),
)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/ping", tags=["system"])
async def ping():
    return "pong"


app.include_router(config_router)