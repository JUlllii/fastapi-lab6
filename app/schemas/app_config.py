from pydantic import BaseModel, Field


class AppConfigModel(BaseModel):
    app_name: str = Field(..., description="Название приложения")
    app_version: str = Field(..., description="Версия приложения")
    app_description: str = Field(..., description="Описание приложения")
    app_authors: list[str] = Field(default_factory=list, description="Авторы")