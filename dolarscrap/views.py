from django.shortcuts import render
from django.views.generic import ListView

from dolarscrap.models import Dollar


def index(request):
    dollars = Dollar.objects.all()
    return render(request, 'dolarscrap/dollar_list.html', {'dollars': dollars})

# Solo para referencia
# class IndexView(ListView):
#     model = Dollar
#     context_object_name = 'dollars'
