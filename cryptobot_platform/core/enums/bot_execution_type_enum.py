from django.db import models


class BotExecutionType(models.IntegerChoices):
    ONCE = 0
    WEEKLY = 1
    DAILY = 2
    HOURLY = 3
    MINUTE = 4
    ASAP = 5
