from __future__ import annotations
from typing import Container, List, Optional
from core.enums.bot_run_status_enum import BotRunStatus
import docker
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.models import Bot

from docker.errors import NotFound


class ContainerManager:
    docker_client = docker.from_env()

    @staticmethod
    def start_container(bot: Bot) -> None:
        if bot.container_id:
            container = ContainerManager.get_container(bot.container_id)
            container.start()
        else:
            container = ContainerManager.docker_client.containers.run(
                "ubuntu", detach=True)
            bot.container_id = container.id
            bot.save()

    @staticmethod
    def stop_container(bot: Bot) -> None:
        container = ContainerManager.get_container(bot.container_id)
        container.stop()

    @staticmethod
    def get_container(id: str) -> Container:
        return ContainerManager.docker_client.containers.get(id)
