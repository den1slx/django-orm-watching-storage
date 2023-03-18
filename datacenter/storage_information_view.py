from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_long_visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        h, m = format_duration(get_duration(visit))
        visit_info = {}
        visit_info['who_entered'] = visit.passcard.owner_name
        visit_info['entered_at'] = visit.entered_at
        visit_info['duration'] = f'{h}:{m}'
        visit_info['is_strange'] = is_long_visit(visit, h=1)
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
