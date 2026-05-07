from fastapi import Depends, Request
from app.schemas.app_config import AppConfigModel
from app.services.runtime_config_service import RuntimeConfigService


def get_dependency_container(request: Request):
    return request.app.state.deps


def get_app_config(
    container=Depends(get_dependency_container),
) -> AppConfigModel:
    return container.get_dependency("app_config")


def get_runtime_config_service(
    container=Depends(get_dependency_container),
) -> RuntimeConfigService:
    return container.get_dependency("runtime_config_service")