from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Bot
from django.http import HttpResponse
from core.utils.helper_functions import provide_uuid1_string
from core.enums.bot_execution_type_enum import BotExecutionType
from core.enums.bot_run_status_enum import BotRunStatus
from django.shortcuts import redirect
from django.shortcuts import render
from core.enums.bot_run_status_enum import BotRunStatus
from core.containers.container_manager import ContainerManager

# Create your views here.


@login_required
def create_bot(request) -> HttpResponse:
    id = provide_uuid1_string()
    owner = request.user
    print(owner)
    execution_type = BotExecutionType.ONCE
    bot = Bot(id=id, owner=owner,
              execution_type=execution_type)
    bot.save()
    return redirect('bot_list')


@login_required
def bot_list(request) -> HttpResponse:
    bots = Bot.objects.filter(owner=request.user)
    for b in bots:
        if b.container_id:
            status = ContainerManager.get_container(b.container_id).status
        else:
            status = "NO STATUS"
        b.status = status
    return render(request, 'bot_list.html', {"bots": bots})


@login_required
def start_bot(request, id: str) -> HttpResponse:
    bot: Bot = Bot.objects.get(id=id)
    bot.start_bot()
    return redirect('bot_list')


@login_required
def stop_bot(request, id: str) -> HttpResponse:
    bot: Bot = Bot.objects.get(id=id)
    bot.stop_bot()
    return redirect('bot_list')
