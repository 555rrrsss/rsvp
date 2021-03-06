# Generated by Django 3.1.2 on 2020-11-29 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import optimized_image.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Event title.', max_length=100)),
                ('slug', models.SlugField(help_text='Event URL.', max_length=150, unique=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', help_text='Status of Event.', max_length=6)),
                ('booking_deadline', models.DateField(help_text='Event deadline.')),
                ('availability', models.CharField(choices=[('Unlimited', 'Unlimited'), ('Limited', 'Limited')], default='Unlimited', help_text='If event is space limited.', max_length=10)),
                ('slots', models.IntegerField(blank=True, help_text="Number of slots if availability is marked as 'limited'.", null=True)),
                ('description', models.TextField(help_text='Event description.', max_length=1000)),
                ('important_note', models.TextField(blank=True, help_text='Important information or notes regarding the event.', null=True)),
                ('start_date', models.DateTimeField(help_text='Event start date.')),
                ('end_date', models.DateTimeField(blank=True, help_text='Event end date, if any.', null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Occurrence of the most recent update to this subsection.')),
                ('image', optimized_image.fields.OptimizedImageField(help_text='Event cover image.', upload_to='events/images/general_events/')),
                ('adult_fee', models.DecimalField(decimal_places=2, default='0', help_text='Event fee for Adults, per slot.', max_digits=6, max_length=20)),
                ('kids_fee', models.DecimalField(decimal_places=2, default='0', help_text='Event fee for Kids, per slot.', max_digits=6, max_length=20)),
            ],
            options={
                'verbose_name': 'General Event',
                'verbose_name_plural': 'General Events',
            },
        ),
        migrations.CreateModel(
            name='YouthEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Event title.', max_length=100)),
                ('slug', models.SlugField(help_text='Event URL.', max_length=150, unique=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', help_text='Status of Event.', max_length=6)),
                ('booking_deadline', models.DateField(help_text='Event deadline.')),
                ('availability', models.CharField(choices=[('Unlimited', 'Unlimited'), ('Limited', 'Limited')], default='Unlimited', help_text='If event is space limited.', max_length=10)),
                ('slots', models.IntegerField(blank=True, help_text="Number of slots if availability is marked as 'limited'.", null=True)),
                ('description', models.TextField(help_text='Event description.', max_length=1000)),
                ('important_note', models.TextField(blank=True, help_text='Important information or notes regarding the event.', null=True)),
                ('start_date', models.DateTimeField(help_text='Event start date.')),
                ('end_date', models.DateTimeField(blank=True, help_text='Event end date, if any.', null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Occurrence of the most recent update to this subsection.')),
                ('image', optimized_image.fields.OptimizedImageField(help_text='Event cover image.', upload_to='events/images/youth_events/')),
                ('age_group', models.CharField(choices=[('All', 'All'), ('Young Adults', 'Young Adults'), ('Teens', 'Teens'), ('Kids', 'Kids')], default='All', help_text='Age group in which Event is intended for.', max_length=50)),
                ('fee', models.DecimalField(decimal_places=2, default='0', help_text='Event Fee per slot.', max_digits=6, max_length=20)),
            ],
            options={
                'verbose_name': 'Youth Event',
                'verbose_name_plural': 'Youth Events',
            },
        ),
        migrations.CreateModel(
            name='YouthEventBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Your first name.', max_length=50)),
                ('last_name', models.CharField(help_text='Your last name.', max_length=50)),
                ('email', models.EmailField(help_text='Main e-mail address.', max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number, mobile or landline.', max_length=15, region=None)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation.')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Occurrence of the most recent update to this booking.')),
                ('bookings', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', help_text='Number of attendees.', max_length=50)),
                ('event', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.youthevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bookings',
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='YouthEventAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineup', models.CharField(help_text='Agenda title.', max_length=100)),
                ('date', models.DateField(blank=True, help_text='Date of occurrence.', null=True)),
                ('start_time', models.TimeField(blank=True, help_text='Time of occurrence.', null=True)),
                ('end_time', models.TimeField(blank=True, help_text='Estimated end time.', null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Occurrence of the most recent update to this subsection.')),
                ('youth_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.youthevent')),
            ],
            options={
                'verbose_name': 'Youth event agenda',
                'verbose_name_plural': 'Youth event Agenda',
            },
        ),
        migrations.CreateModel(
            name='GeneralEventBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Your first name.', max_length=50)),
                ('last_name', models.CharField(help_text='Your last name.', max_length=50)),
                ('email', models.EmailField(help_text='Main e-mail address.', max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number, mobile or landline.', max_length=15, region=None)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation.')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Occurrence of the most recent update to this booking.')),
                ('adult_bookings', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', help_text='Number of Adults.', max_length=3)),
                ('children_bookings', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', help_text='Number of Children.', max_length=3)),
                ('event', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.generalevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bookings',
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='GeneralEventAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineup', models.CharField(help_text='Agenda title.', max_length=100)),
                ('date', models.DateField(blank=True, help_text='Date of occurrence.', null=True)),
                ('start_time', models.TimeField(blank=True, help_text='Time of occurrence.', null=True)),
                ('end_time', models.TimeField(blank=True, help_text='Estimated end time.', null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Date of creation.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Occurrence of the most recent update to this subsection.')),
                ('general_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.generalevent')),
            ],
            options={
                'verbose_name': 'General event agenda',
                'verbose_name_plural': 'General event Agenda',
            },
        ),
    ]
