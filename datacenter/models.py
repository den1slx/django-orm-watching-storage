from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def time_to_seconds(h=0, m=0, s=0):
    h = int(h) * 3600
    m = int(m) * 60
    s = int(s)
    seconds = h + m + s
    return seconds


def is_long_visit(visit, m=0, h=0):
    if not visit.leaved_at:
        return get_duration(visit) >= (time_to_seconds(m) + time_to_seconds(h))
    delta = visit.leaved_at - visit.entered_at
    delta = delta.total_seconds()
    return delta >= time_to_seconds(m=m, h=h)


def get_duration(visit):
    if not visit.leaved_at:
        time = timezone.localtime()
        delta = time - visit.entered_at
        return delta.total_seconds()
    delta = visit.leaved_at - visit.entered_at
    return delta.total_seconds()


def format_duration(duration, type_tuple=False):
    h = int(duration // 3600)
    m = int((duration % 3600) // 60)
    if h < 10:
        h = f'0{h}'
    if m < 10:
        m = f'0{m}'
    if type_tuple:
        return h, m
    return f'{h}:{m}'
