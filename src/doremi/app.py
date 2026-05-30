from __future__ import annotations
import logging

from .config import Config

logger = logging.getLogger(__name__)


class DoremiApp:
    def __init__(self, config: Config | None = None) -> None:
        self.config = config or Config.from_env()
        self._configure_logging()

    def _configure_logging(self) -> None:
        level = logging.DEBUG if self.config.debug else logging.INFO
        logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    def run(self) -> None:
        logger.info("Starting Doremi assistant")
        logger.debug("Configuration: %s", self.config)
        # TODO: implement the main voice assistant workflow.
        logger.info("Doremi is ready to process commands")


def main() -> None:
    DoremiApp().run()
