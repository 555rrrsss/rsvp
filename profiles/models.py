from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, blank=True,
                              choices=GENDER_CHOICES, help_text="Your gender")
    date_of_birth = models.DateField(
        blank=True, null=True, help_text="Date, Month and birth Year")
    phone = PhoneNumberField(max_length=256, blank=True,
                             null=True, help_text="Phone number, mobile or landline")
    Address = models.CharField(blank=True, max_length=150, help_text='Address')
    city = models.CharField(blank=True, max_length=50,
                            help_text='City / Town / Village')
    province = models.CharField(
        blank=True, max_length=50, help_text='County / State / Province')
    country = CountryField(blank_label='(Select country)',
                           default="IE", blank=True, help_text='Country of residency')
    postal_code = models.CharField(
        blank=True, max_length=20, help_text='Postal Code / Eircode')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
