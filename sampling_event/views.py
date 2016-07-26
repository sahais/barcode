from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import sampleEvent, sample, plate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

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


class sampleEventCreate(CreateView):
    model = sampleEvent
    fields = ['date', 'assayName', 'coge', 'samplers', 'site', 'facility', 'environment', 'spacecraft']


class sampleEventUpdate(UpdateView):
    model = sampleEvent
    fields = ['date', 'assayName', 'coge', 'samplers', 'site', 'facility', 'environment', 'spacecraft']


class sampleEventDelete(DeleteView):
    model = sampleEvent
    success_url = reverse_lazy('sampling_event:index')






def sampleIndex(request, pk):
    sampleTemp = get_object_or_404(sample, pk=pk)
    return render(request, 'sampling_event/sample.html', {'sampleTemp': sampleTemp})


class sampleCreate(CreateView):
    model = sample
    fields = ['samplingEvent', 'sampleType', 'serialNumber', 'accountable', 'description']


class sampleUpdate(UpdateView):
    model = sample
    fields = ['sampleType', 'serialNumber', 'accountable', 'description']


class sampleDelete(DeleteView):
    model = sample
    success_url = reverse_lazy('sampling_event:detail')


class UserFormView(View):
    form_class = UserForm
    template_name = 'sampling_event/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned/ normalized data
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credientials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('sampling_event:index')

        return render(request, self.template_name, {'form': form})




