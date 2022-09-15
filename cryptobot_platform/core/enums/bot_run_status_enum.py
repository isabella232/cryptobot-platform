from django.db import models


class BotRunStatus(models.IntegerChoices):
    STOPPED = 0
    RUNNING = 1
    ERROR = 2
