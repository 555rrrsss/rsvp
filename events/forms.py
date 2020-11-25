from django import forms
from crispy_forms.helper import FormHelper

from .models import *


# General Events form
class GeneralEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GeneralEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True

    class Meta:
        model = GeneralEventBooking
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'adult_bookings', 'children_bookings',)


# Youth Events form
class YouthEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(YouthEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True

    class Meta:
        model = YouthEventBooking
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'bookings',)
