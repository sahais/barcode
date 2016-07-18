from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import sampleEvent, sample, plate
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
"""
class IndexView(generic.ListView):
    template_name = 'sampling_event/index.html'

    def get_queryset(self):
        return sampleEvent.objects.all()


class DetailView(generic.DetailView):
    model = sampleEvent
    template_name = 'sampling_event/detail.html'

"""


def index(request):
    all_sampleEvents = sampleEvent.objects.all()
    context = {'all_sampleEvents' : all_sampleEvents,}
    return render(request, 'sampling_event/index.html', context)


def detail(request, sampleEvent_id):
    sampleEven = get_object_or_404(sampleEvent, pk = sampleEvent_id)
    return render(request, 'sampling_event/detail.html', {'sampleEvent': sampleEven,})


def delete_sampleEvent(request, event_id):
    event = sampleEvent.objects.get(pk = event_id)
    event.delete()
    return render(request, 'sampling_event/index.html', )





class sampleEventCreate(CreateView):
    model = sampleEvent
    fields = ['date', 'assayName', 'coge', 'samplers', 'site', 'facility', 'environment', 'spacecraft']


class sampleEventUpdate(UpdateView):
    model = sampleEvent
    fields = ['date', 'assayName', 'coge', 'samplers', 'site', 'facility', 'environment', 'spacecraft']


class sampleEventDelete(DeleteView):
    model = sampleEvent
    success_url = reverse_lazy('sampling_event: index')