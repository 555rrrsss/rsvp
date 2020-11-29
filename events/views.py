from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, redirect

from .models import *
from .forms import *

# Create your views here.


# EVENTS INDEX -------------------------------------------------------------------------


# Events
def index(request):
    return render(request, 'events/events_booking/events.html',)


# GENERAL EVENTS ----------------------------------------------------------------------


# General Events
def general_events(request):
    events = GeneralEvent.objects.all().order_by("-created")
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
    return render(request, 'events/events_booking/general_events/general_events_list.html', args)


# General Events Booking
def general_events_booking(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    # initial form values
    initial = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'phone_number': request.user.profile.phone
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
    if event.is_closed_for_bookings():
        event.status = 'Closed'
        event.save()
    args = {'event': event, 'form': form}
    return render(request, 'events/events_booking/general_events/general_event_detail.html', args)


# General Events Booking Complete
def general_events_booking_complete(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    event_booking = GeneralEventBooking.objects.get(event__slug=slug)
    args = {'event': event, 'event_booking': event_booking}
    return render(request, 'events/events_booking/general_events/general_event_complete.html', args)


# General Event User Bookings List
def general_events_user_bookings_list(request):
    event_bookings = GeneralEventBooking.objects.filter(user=request.user).order_by("-event__created")
    # paginator
    paginator = Paginator(event_bookings, 10)  # Show # per page
    page = request.GET.get('page')
    event_bookings = paginator.get_page(page)
    args = {'event_bookings': event_bookings}
    return render(request, 'events/user_bookings/general_event_bookings/general_events_user_bookings_list.html', args)


# General Event User Booking Detail
def general_event_user_booking_detail(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    event_booking = GeneralEventBooking.objects.get(event__slug=slug)
    # Delete User Booking
    if request.method == "POST":
        event_booking.delete()
        return redirect('general_events_user_bookings_list')
    args = {'event': event,
            'event_booking': event_booking, }
    return render(request, 'events/user_bookings/general_event_bookings/general_event_user_booking_detail.html', args)


# General Events User Booking Modify
def general_events_booking_modify(request, slug):
    event = GeneralEventBooking.objects.get(event__slug=slug)
    # form
    form = GeneralEventForm(instance=event)
    if request.method == 'POST':
        form = GeneralEventForm(request.POST, instance=event)
        if form.is_valid():
            form = form.save(commit=True)
            form.user = request.user
            form.save()
            return redirect('general_events_booking_modify_complete', slug=event.event.slug)
    else:
        form = GeneralEventForm(instance=event)
    args = {'event': event, 'form': form}
    return render(request, 'events/user_bookings/general_event_bookings/general_event_modify.html', args)


# General Events User Booking Modify Complete
def general_events_booking_modify_complete(request, slug):
    event = get_object_or_404(GeneralEvent, slug=slug)
    event_booking = GeneralEventBooking.objects.get(event__slug=slug)
    args = {'event': event, 'event_booking': event_booking}
    return render(request, 'events/user_bookings/general_event_bookings/general_event_modify_complete.html', args)


# YOUTH EVENTS ------------------------------------------------------------------------


# Youth Events
def youth_events(request):
    events = YouthEvent.objects.all().order_by("-created")
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
    return render(request, 'events/events_booking/youth_events/youth_events_list.html', args)


# Youth Events Booking
def youth_events_booking(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    # initial form values
    initial = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'phone_number': request.user.profile.phone
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
    return render(request, 'events/events_booking/youth_events/youth_event_detail.html', args)


# Youth Events Booking Complete
def youth_events_booking_complete(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    event_booking = YouthEventBooking.objects.get(event__slug=slug)
    args = {'event': event, 'event_booking': event_booking}
    return render(request, 'events/events_booking/youth_events/youth_event_complete.html', args)


# Youth Event User Bookings List
def youth_events_user_bookings_list(request):
    event_bookings = YouthEventBooking.objects.filter(user=request.user).order_by("-event__created")
    # paginator
    paginator = Paginator(event_bookings, 10)  # Show # per page
    page = request.GET.get('page')
    event_bookings = paginator.get_page(page)
    args = {'event_bookings': event_bookings}
    return render(request, 'events/user_bookings/youth_event_bookings/youth_events_user_bookings_list.html', args)


# Youth Event User Booking Detail
def youth_event_user_booking_detail(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    event_booking = YouthEventBooking.objects.get(event__slug=slug)
    # Delete User Booking
    if request.method == "POST":
        event_booking.delete()
        return redirect('youth_events_user_bookings_list')
    args = {'event': event,
            'event_booking': event_booking, }
    return render(request, 'events/user_bookings/youth_event_bookings/youth_event_user_booking_detail.html', args)


# Youth Events User Booking Modify
def youth_events_booking_modify(request, slug):
    event = YouthEventBooking.objects.get(event__slug=slug)
    # form
    form = YouthEventForm(instance=event)
    if request.method == 'POST':
        form = YouthEventForm(request.POST, instance=event)
        if form.is_valid():
            form = form.save(commit=True)
            form.user = request.user
            form.save()
            return redirect('youth_events_booking_modify_complete', slug=event.event.slug)
    else:
        form = YouthEventForm(instance=event)
    args = {'event': event, 'form': form}
    return render(request, 'events/user_bookings/youth_event_bookings/youth_event_modify.html', args)


# Youth Events User Booking Modify Complete
def youth_events_booking_modify_complete(request, slug):
    event = get_object_or_404(YouthEvent, slug=slug)
    event_booking = YouthEventBooking.objects.get(event__slug=slug)
    args = {'event': event, 'event_booking': event_booking}
    return render(request, 'events/user_bookings/youth_event_bookings/youth_event_modify_complete.html', args)