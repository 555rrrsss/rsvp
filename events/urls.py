from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Events User Bookings
    path('events/bookings', views.events_user_bookings,
         name='events_user_bookings'),
    # General Events
    path('events/general-events', views.general_events, name='general_events'),
    path('events/general-events/<slug>/booking',
         views.general_events_booking, name='general_events_booking'),
    path('events/general-events/<slug>/booking/complete',
         views.general_events_booking_complete, name='general_events_booking_complete'),
    # Youth Events
    path('events/youth-events', views.youth_events, name='youth_events'),
    path('events/youth-events/<slug>/booking',
         views.youth_events_booking, name='youth_events_booking'),
    path('events/youth-events/<slug>/booking/complete',
         views.youth_events_booking_complete, name='youth_events_booking_complete'),
]
