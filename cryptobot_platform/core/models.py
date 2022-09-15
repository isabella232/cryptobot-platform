from django.db import models
from django.contrib.auth.models import User
from core.enums.bot_execution_type_enum import BotExecutionType
from core.enums.bot_run_status_enum import BotRunStatus

# Create your models here.


class CryptoBot(models.Model):
    id = models.CharField(max_length=50, primary_key=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    execution_type = models.IntegerField(null=False, choices=BotExecutionType.choices)
    run_status = models.IntegerField(null=False, choices=BotRunStatus.choices)
