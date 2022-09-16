from typing import Container
from django.db import models
from django.contrib.auth.models import User
from core.enums.bot_execution_type_enum import BotExecutionType
from core.enums.bot_run_status_enum import BotRunStatus
from core.containers.container_manager import ContainerManager
import docker
from typing import Any, Optional
# Create your models here.


class Bot(models.Model):
    id = models.CharField(max_length=50, primary_key=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    execution_type = models.IntegerField(
        null=False, choices=BotExecutionType.choices)
    container_id = models.CharField(max_length=50, null=True)

    def start_bot(self) -> None:
        ContainerManager.start_container(self)

    def stop_bot(self) -> None:
        ContainerManager.stop_container(self)
