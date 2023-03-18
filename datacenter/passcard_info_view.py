from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_long_visit
from datacenter.models import format_duration
from datacenter.models import get_duration
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcards = Passcard.objects.all()
    passcard = get_object_or_404(passcards, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        visit_info = {}
        h, m = format_duration(get_duration(visit))
        visit_info['entered_at'] = visit.entered_at
        visit_info['duration'] = f'{h}:{m}'
        visit_info['is_strange'] = is_long_visit(visit, h=1)
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
