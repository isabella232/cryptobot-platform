from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import CryptoBot
from django.http import HttpResponse
from core.utils.helper_functions import provide_uuid1_string
from core.enums.bot_execution_type_enum import BotExecutionType
from core.enums.bot_run_status_enum import BotRunStatus
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.


@login_required
def create_bot(request) -> HttpResponse:
    id = provide_uuid1_string()
    owner = request.user
    print(owner)
    execution_type = BotExecutionType.ONCE
    run_status = BotRunStatus.STOPPED
    bot = CryptoBot(id=id, owner=owner,
                    execution_type=execution_type, run_status=run_status)
    bot.save()
    return redirect('show_bots')


@login_required
def bot_list(request) -> HttpResponse:
    bots = CryptoBot.objects.filter(owner=request.user)
    return render(request, 'bot_list.html', {"bots": bots})


@login_required
def start_bot(request, id: str) -> HttpResponse:
    bot = CryptoBot.objects.get(id=id)
    return HttpResponse(f"Found bot {id}")
