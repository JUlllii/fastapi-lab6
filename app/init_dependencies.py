from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel
from app.services.runtime_config_service import RuntimeConfigService


class DependencyContainer(dict):
    def get_dependency(self, key: str):
        if key not in self:
            raise KeyError(f"Зависимость '{key}' не найдена")
        return self[key]


def init_dependencies() -> DependencyContainer:
    app_config = AppConfigModel(
        app_name="Laboratory FastAPI App",
        app_version="1.0.0",
        app_description="Учебное приложение на FastAPI",
        app_authors=["Иванов И.И.", "Петров П.П."],
    )
    runtime_config_service = RuntimeConfigService(
        initial_config=RuntimeConfigModel()
    )
    container = DependencyContainer()
    container["app_config"] = app_config
    container["runtime_config_service"] = runtime_config_service
    return container