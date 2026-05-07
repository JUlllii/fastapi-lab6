from typing import Literal
from pydantic import BaseModel, Field

LOG_LEVELS = Literal["DEBUG", "INFO", "WARNING", "ERROR"]


class RuntimeConfigModel(BaseModel):
    log_level: LOG_LEVELS = Field(default="INFO")
    feature_flag: bool = Field(default=False)
    maintenance_mode: bool = Field(default=False)
    runtime_message: str = Field(default="Приложение работает в штатном режиме")


class RuntimeConfigUpdateModel(BaseModel):
    log_level: LOG_LEVELS = Field(...)
    feature_flag: bool = Field(...)
    maintenance_mode: bool = Field(...)
    runtime_message: str = Field(...)