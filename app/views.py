import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Person


def add_person(request):
    for i in range(20):
        person = Person()
        flag = random.randrange(100)
        person.p_name = 'tom%d' % flag
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse('批量创建成功')


def person_list(request):
    person = Person.objects.exclude(p_age__gt=50)
    context = {
        'person': person
    }
    return render(request, 'person_list.html', context=context)
