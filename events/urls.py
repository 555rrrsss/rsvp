from django.urls import path

from . import views

urlpatterns = [
     
     path('', views.index, name='index'),

    # EVENTS BOOKING ------------------------------------------------------------------------------------------------- 
   
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

    # USER BOOKINGS ------------------------------------------------------------------------------------------------- 
    
    # General Events User Bookings
    path('events/bookings/general-events/', views.general_events_user_bookings_list,
         name='general_events_user_bookings_list'),
    path('events/bookings/general-events/<slug>', views.general_event_user_booking_detail,
         name='general_event_user_booking_detail'),
    path('events/bookings/general-events/<slug>/modify',
         views.general_events_booking_modify, name='general_events_booking_modify'),
    path('events/bookings/general-events/<slug>/modify/complete',
         views.general_events_booking_modify_complete, name='general_events_booking_modify_complete'),
    # Youth Events User Bookings
    path('events/bookings/youth-events/', views.youth_events_user_bookings_list,
         name='youth_events_user_bookings_list'),
    path('events/bookings/youth-events/<slug>', views.youth_event_user_booking_detail,
         name='youth_event_user_booking_detail'),
    path('events/bookings/youth-events/<slug>/modify',
         views.youth_events_booking_modify, name='youth_events_booking_modify'),
    path('events/bookings/youth-events/<slug>/modify/complete',
         views.youth_events_booking_modify_complete, name='youth_events_booking_modify_complete'),
]
