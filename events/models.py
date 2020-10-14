from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from rsvp.utils import unique_slug_generator
from optimized_image.fields import OptimizedImageField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


# BASE MODELS -------------------------------------------------------------------------

# Base Event Agenda
class BaseEventAgenda(models.Model):
    lineup = models.CharField(
        max_length=100, help_text="Agenda title.")
    date = models.DateField(blank=True, null=True,
                            help_text="Date of occurrence.")
    start_time = models.TimeField(
        blank=True, null=True, help_text="Time of occurrence.")
    end_time = models.TimeField(
        blank=True, null=True, help_text="Estimated end time.")
    created = models.DateTimeField(
        default=timezone.now, help_text="Date of creation.")
    modified = models.DateTimeField(
        auto_now=True, help_text="Occurrence of the most recent update to this subsection.")

    def __str__(self):
        return self.lineup

    class Meta:
        abstract = True


# Base Event
class BaseEvent(models.Model):
    title = models.CharField(max_length=100, help_text="Event title.")
    slug = models.SlugField(max_length=150, unique=True,
                            help_text="Event URL.")
    status_choices = (
        ('Open', 'Open'),
        ('Closed', 'Closed')
    )
    status = models.CharField(
        max_length=6, choices=status_choices, default='Open', help_text="Status of Event.")
    booking_deadline = models.DateField(
        blank=False, null=False, help_text="Event deadline.")
    availability_choices = (
        ('Unlimited', 'Unlimited'),
        ('Limited', 'Limited')
    )
    availability = models.CharField(
        max_length=10, choices=availability_choices, default='Unlimited', help_text="If event is space limited.")
    slots = models.IntegerField(
        null=True, blank=True, help_text="Number of slots if availability is marked as 'limited'.")
    description = models.TextField(
        max_length=1000, help_text="Event description.")
    important_note = models.TextField(
        null=True, blank=True, help_text="Important information or notes regarding the event.")
    start_date = models.DateTimeField(help_text="Event start date.")
    end_date = models.DateTimeField(
        blank=True, null=True, help_text="Event end date, if any.")
    created = models.DateTimeField(
        default=timezone.now, help_text="Date of creation.")
    modified = models.DateTimeField(
        auto_now=True, help_text="Occurrence of the most recent update to this subsection.")

    def booking_deadline_has_passed(self):
        return self.booking_deadline > datetime.date.today()

    def is_limited(self):
        return self.availability == 'Limited'

    # def is_full(self):
    #     return self.is_limited and self.baseeventbooking_set.all().count() >= self.slots

    # def is_closed_for_bookings(self):
    #     return True if self.is_full() or self.booking_deadline_has_passed() else False

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


# Base Event Form Model
class BaseEventBooking(models.Model):
    full_name = models.CharField(
        max_length=50, help_text="Your full name.")
    email = models.EmailField(max_length=50, help_text="Main e-mail address.")
    phone_number = PhoneNumberField(
        max_length=15, help_text="Phone number, mobile or landline.")
    booking_date = models.DateTimeField(
        default=timezone.now, help_text="Date of booking.")

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


# GENERAL EVENTS ----------------------------------------------------------------------

# General Event Agenda
class GeneralEventAgenda(BaseEventAgenda):
    general_event = models.ForeignKey('GeneralEvent', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'General event agenda'
        verbose_name_plural = 'General event Agenda'


# General Event
class GeneralEvent(BaseEvent):
    image = OptimizedImageField(
        upload_to='events/images/general_events/', blank=False, null=False, help_text="Event cover image.")
    adult_fee = models.DecimalField(
        max_length=20, max_digits=6, decimal_places=2, default='0', help_text="Event fee for Adults, per slot.")
    kids_fee = models.DecimalField(
        max_length=20, max_digits=6, decimal_places=2, default='0', help_text="Event fee for Kids, per slot.")

    class Meta():
        verbose_name = 'General Event'
        verbose_name_plural = 'General Events'


# General Event Form Model
class GeneralEventBooking(BaseEventBooking):
    event = models.ForeignKey(
        GeneralEvent, default=None, null=True, on_delete=models.CASCADE)
    adult_bookings_choices = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    adult_bookings = models.CharField(
        max_length=3, choices=adult_bookings_choices, default='0', help_text="Number of Adults.")
    children_bookings_choices = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    children_bookings = models.CharField(
        max_length=3, choices=children_bookings_choices, default='0', help_text="Number of Children.")

    class Meta():
        verbose_name = 'Bookings'
        verbose_name_plural = 'Bookings'


# YOUTH EVENTS ------------------------------------------------------------------------

# Youth Event Agenda
class YouthEventAgenda(BaseEventAgenda):
    youth_event = models.ForeignKey('YouthEvent', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Youth event agenda'
        verbose_name_plural = 'Youth event Agenda'


# Youth Event
class YouthEvent(BaseEvent):
    image = OptimizedImageField(upload_to='events/images/youth_events/',
                                blank=False, null=False, help_text="Event cover image.")
    age_group_choices = (
        ('All', 'All'),
        ('Young Adults', 'Young Adults'),
        ('Teens', 'Teens'),
        ('Kids', 'Kids')
    )
    age_group = models.CharField(
        max_length=50, choices=age_group_choices, default='All', help_text="Age group in which Event is intended for.")
    fee = models.DecimalField(
        max_length=20, max_digits=6, decimal_places=2, default='0', help_text="Event Fee per slot.")

    class Meta():
        verbose_name = 'Youth Event'
        verbose_name_plural = 'Youth Events'


# Youth Event Form Model
class YouthEventBooking(BaseEventBooking):
    event = models.ForeignKey(YouthEvent, default=None,
                              null=True, on_delete=models.CASCADE)
    bookings_choices = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    bookings = models.CharField(
        max_length=50, choices=bookings_choices, default='0', help_text="Number of attendees.")

    class Meta():
        verbose_name = 'Bookings'
        verbose_name_plural = 'Bookings'


# OTHER --------------------------------------------------------------------------------

# Slug


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title)


def save(self, *args, **kwargs):
    self.s = slugify(self.q)
    super(Test, self).save(*args, **kwargs)


pre_save.connect(slug_save, sender=GeneralEvent)
pre_save.connect(slug_save, sender=YouthEvent)
