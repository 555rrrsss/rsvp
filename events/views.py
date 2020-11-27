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
    general_event_bookings = GeneralEventBooking.objects.filter(user=request.user)
    youth_event_bookings = YouthEventBooking.objects.filter(user=request.user)
    args = {'general_events': general_events, 'general_event_bookings': general_event_bookings,
            'youth_events': youth_events, 'youth_event_bookings': youth_event_bookings,}
    return render(request, 'events/user_bookings/event-bookings.html', args)


# User General Event Bookings
def events_user_booking_general_event_info(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    general_event_booking = GeneralEventBooking.objects.filter(event=event, user=request.user)
    if request.method== "POST":
        general_event_booking.delete()
        return redirect('events_user_bookings')
    args = {'event': event,
            'general_event_booking': general_event_booking,}
    return render(request, 'events/user_bookings/event-booking-general-event-info.html', args)


# User Youth Event Bookings
def events_user_booking_youth_event_info(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    youth_event_booking = YouthEventBooking.objects.filter(event=event, user=request.user)
    if request.method== "POST":
        youth_event_booking.delete()
        return redirect('events_user_bookings')
    args = {'event': event,
            'youth_event_booking': youth_event_booking,}
    return render(request, 'events/user_bookings/event-booking-youth-event-info.html', args)


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


# General Events Booking
def general_events_booking(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    # initial form values
    initial = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'phone_number': request.user.userprofile.phone
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


# General Events Booking Complete
def general_events_booking_complete(request, slug):
    event_complete = get_object_or_404(GeneralEvent, slug=slug)
    args = {'event_complete': event_complete}
    return render(request, 'events/general_events/general_event_complete.html', args)


# General Events Booking Modify
def general_events_booking_modify(request, slug):
    event = GeneralEventBooking.objects.get(event__slug=slug)
    # form
    form = GeneralEventForm(instance=event)
    if request.method == 'POST':
        form = GeneralEventForm(instance=event)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            form.user = request.user
            form.save()
            return redirect('events_user_booking_general_event_info', slug=event.slug)
    args = {'event': event, 'form': form}
    return render(request, 'events/general_events/general_event_modify.html', args)

    
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


# Youth Events Booking
def youth_events_booking(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    # inital form values
    initial = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'phone_number': request.user.userprofile.phone
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


# Youth Events Booking Complete
def youth_events_booking_complete(request, slug):
    event_complete = get_object_or_404(YouthEvent, slug=slug)
    args = {'event_complete': event_complete}
    return render(request, 'events/youth_events/youth_event_complete.html', args)


# Modify Youth Events Booking
def youth_events_booking_modify(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    form =  YouthEventForm(instance=event)
    # form
    if request.method == 'POST':
        form = YouthEventForm(request.POST, instance=event)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            form.user = request.user
            form.save()
            return redirect('events_user_booking_youth_event_info', slug=event.slug)
    args = {'event': event, 'form': form}
    return render(request, 'events/youth_events/youth_event_modify.html', args)

