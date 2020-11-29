from django.contrib import admin

from .models import *

# Register your models here.


# General Event Agenda Inline
class GeneralEventAgendaInline(admin.TabularInline):
    model = GeneralEventAgenda
    fields = ['lineup', 'date', 'start_time',
              'end_time']


# General Event Booking Inline
class GeneralEventBookingInline(admin.TabularInline):
    model = GeneralEventBooking
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
                    'adult_bookings', 'children_bookings',)
    readonly_fields = ['booking_date', 'modified_date']

# General Event
class GeneralEventAdmin(admin.ModelAdmin):
    inlines = [GeneralEventAgendaInline, GeneralEventBookingInline, ]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'status', 'start_date',)
    search_fields = ('title', 'status',)
    list_filter = ('status',)
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
    fields = ['title', 'slug', 'image', 'status', 'booking_deadline', 'availability',
              'slots', 'description', 'important_note', 'start_date', 'end_date', 'adult_fee', 'kids_fee', 'created']


admin.site.register(GeneralEvent, GeneralEventAdmin)


# Youth Event Agenda Inline
class YouthEventAgendaInline(admin.TabularInline):
    model = YouthEventAgenda
    fields = ['lineup', 'date', 'start_time', 'end_time']


# Youth Event Booking Inline
class YouthEventBookingInline(admin.TabularInline):
    model = YouthEventBooking
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'bookings',)
    readonly_fields = ['booking_date', 'modified_date']


# Youth Event
class YouthEventAdmin(admin.ModelAdmin):
    inlines = [YouthEventAgendaInline, YouthEventBookingInline, ]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'status', 'age_group',
                    'start_date',)
    search_fields = ('title', 'status',)
    list_filter = ('status',)
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
    fields = ['title', 'slug', 'image', 'status', 'booking_deadline', 'availability',
              'slots', 'description', 'important_note', 'start_date', 'end_date', 'age_group', 'fee']


admin.site.register(YouthEvent, YouthEventAdmin)

