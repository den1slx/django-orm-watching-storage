from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render



def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        visit_info = {}
        visit_info['who_entered'] = visit.passcard
        visit_info['entered_at'] = visit.entered_at
        visit_info['duration'] = format_duration(get_duration(visit))
        non_closed_visits.append(visit_info)


    # non_closed_visits = [
    #     {
    #         'who_entered': 'Richard Shaw',
    #         'entered_at': '11-04-2018 25:34',
    #         'duration': '25:03',
    #     }
    # ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
