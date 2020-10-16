from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.


# Events
def index(request):
    return render(request, 'events/events.html',)


# EVENTS USER BOOKINGS -----------------------------------------------------------------

# User Bookings
def events_user_bookings(request):
    return render(request, 'events/user_bookings/bookings_list.html',)


# GENERAL EVENTS ----------------------------------------------------------------------

# General Events
def general_events(request):
    events = GeneralEvent.objects.all()
    # search
    query = request.GET.get("query")
    if query:
        events = events.filter(
            Q(title__icontains=query)
            | Q(status__icontains=query)
        ).distinct()
    # paginator
    paginator = Paginator(events, 10)  # Show # per page
    page = request.GET.get('page')
    events = paginator.get_page(page)
    args = {'events': events}
    return render(request, 'events/general_events/general_events_list.html', args)


def general_events_booking(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    # initial form values
    initial = {
        'full_name': request.user.get_full_name(),
        'email': request.user.email
    }
    # form
    if request.method == 'POST':
        form = GeneralEventForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            form.user = request.user
            form.save()
            return redirect('general_events_booking_complete', slug=event.slug)
    else:
        form = GeneralEventForm(initial=initial)
    # close event
    # if event.is_closed_for_bookings():
    #     event.status = 'Closed'
    #     event.save()
    args = {'event': event, 'form': form}
    return render(request, 'events/general_events/general_event_detail.html', args)


def general_events_booking_complete(request, slug):
    event_complete = get_object_or_404(GeneralEvent, slug=slug)
    args = {'event_complete': event_complete}
    return render(request, 'events/general_events/general_event_complete.html', args)


# YOUTH EVENTS ------------------------------------------------------------------------

# Youth Events
def youth_events(request):
    events = YouthEvent.objects.all()
    # search
    query = request.GET.get("query")
    if query:
        events = events.filter(
            Q(title__icontains=query)
            | Q(status__icontains=query)
        ).distinct()
    # paginator
    paginator = Paginator(events, 10)  # Show # per page
    page = request.GET.get('page')
    events = paginator.get_page(page)
    args = {'events': events}
    return render(request, 'events/youth_events/youth_events_list.html', args)


def youth_events_booking(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    # inital form values
    initial = {
        'full_name': request.user.get_full_name(),
        'email': request.user.email
    }
    # form
    if request.method == 'POST':
        form = YouthEventForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            form.user = request.user
            form.save()
            return redirect('youth_events_booking_complete', slug=event.slug)
    else:
        form = YouthEventForm(initial=initial)
    # close event
    # if event.is_closed_for_bookings():
    #     event.status = 'Closed'
    #     event.save()
    args = {'event': event, 'form': form}
    return render(request, 'events/youth_events/youth_event_detail.html', args)


def youth_events_booking_complete(request, slug):
    event_complete = get_object_or_404(YouthEvent, slug=slug)
    args = {'event_complete': event_complete}
    return render(request, 'events/youth_events/youth_event_complete.html', args)
