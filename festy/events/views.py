
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.views import View
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from .models import Event
from .forms import EventCreationForm

# Create your views here.

def index(request):
    events_data = Event.objects.all()
    return render(request,'events/index.html',{'events_data':events_data})

# class EventListView(ListView):
#     model = Event
#     template_name = 'events/index.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'events'
#     ordering = ['-event_start_timestamp']


# class EventDetailView(DetailView):
#     model = Event

def event_detail(request,pk):
    obj = get_object_or_404(Event, pk=pk)
    return render(request,'events/event-detail.html',{'object':obj})

@staff_member_required
def ev_create(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            event = form.cleaned_data.get('event_name')
            messages.success(request, f'{event} added!')
            return redirect('events-home')
    else:
        form =EventCreationForm()
    return render(request, 'events/evcreate.html', {'form': form})

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['event_name','description', 'event_start_timestamp', 'event_end_timestamp',
                'event_location_lon','event_location_lat','event_capacity']

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        return True

@login_required
def register(request,pk):
    if request.method == 'POST':
        obj = get_object_or_404(Event, pk=pk)
        if request.user not in obj.event_joinees.all():
            obj.event_joinees.add(request.user)
            obj.save()
            messages.success(request,f'Successfully registered for the event {obj.event_name}')
        else:
            messages.error(request,f'Already registered for the event {obj.event_name}')
        return redirect('events-home')
    return render(request,'events/register.html',{'object':obj})

def deregister(request):
    return render(request,'events/deregister.html')

def registered(request):
    obj = Event.objects.all()
    l = []
    for i in obj:
        if request.user in i.event_joinees.all():
            l.append(i)
    return render(request,'events/registered.html',{'list': l})