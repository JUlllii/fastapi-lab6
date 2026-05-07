from fastapi import APIRouter, Depends
from app.dependencies import get_app_config, get_runtime_config_service
from app.schemas.app_config import AppConfigModel
from app.schemas.responses import HealthResponse
from app.schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel
from app.services.runtime_config_service import RuntimeConfigService

router = APIRouter(tags=["configuration"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/config/app", response_model=AppConfigModel)
def get_app_config_endpoint(
    app_config: AppConfigModel = Depends(get_app_config),
) -> AppConfigModel:
    return app_config


@router.get("/config/runtime", response_model=RuntimeConfigModel)
def get_runtime_config(
    service: RuntimeConfigService = Depends(get_runtime_config_service),
) -> RuntimeConfigModel:
    return service.get_config()


@router.put("/config/runtime", response_model=RuntimeConfigModel)
def update_runtime_config(
    update_data: RuntimeConfigUpdateModel,
    service: RuntimeConfigService = Depends(get_runtime_config_service),
) -> RuntimeConfigModel:
    return service.update_config(update_data)