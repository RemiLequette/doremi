from __future__ import annotations
from dataclasses import dataclass
import os


@dataclass
class Config:
    language: str = "fr"
    debug: bool = False
    assistant_name: str = "doremi"

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            language=os.getenv("DOREMI_LANGUAGE", "fr"),
            debug=os.getenv("DOREMI_DEBUG", "false").lower() in ("1", "true", "yes"),
            assistant_name=os.getenv("DOREMI_NAME", "doremi"),
        )
