# Generated by Django 3.1.2 on 2022-04-19 15:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_cinema_admin', models.BooleanField(default=False)),
                ('is_cinema_accounts', models.BooleanField(default=False)),
                ('is_club', models.BooleanField(default=True)),
                ('is_customer', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_datetime', models.DateTimeField(verbose_name='date logged')),
                ('ticket_quantity', models.IntegerField(default=0)),
                ('is_club_booking', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('age_rating', models.CharField(choices=[('U', 'U'), ('PG', 'PG'), ('12A', '12A'), ('12', '12'), ('15', '15'), ('18', '18')], max_length=3)),
                ('duration', models.DurationField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('screen_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('screen_num', models.IntegerField(max_length=2)),
                ('capacity', models.IntegerField(max_length=3)),
                ('is_full', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('showing_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('showing_time', models.TimeField()),
                ('showing_date', models.DateField()),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.film')),
                ('screen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.screen')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('purchased_datetime', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('street_address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ticket_price', models.FloatField()),
                ('ticket_type', models.CharField(choices=[('Standard', 'Standard'), ('Club', 'Club'), ('Student', 'Student')], max_length=10)),
                ('ticket_quantity', models.IntegerField(default=1)),
                ('showing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.showing')),
            ],
        ),
        migrations.CreateModel(
            name='Statements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.booking')),
            ],
        ),
        migrations.AddField(
            model_name='showing',
            name='venue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.venue'),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('seat_number', models.IntegerField()),
                ('screen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.screen')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='venue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.venue'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('token_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uweflix.token')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=7)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('landline', models.IntegerField(blank=True, null=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CinemaAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_social_distancing', models.BooleanField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='club_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uweflix.club'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uweflix.customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uweflix.ticket'),
        ),
        migrations.CreateModel(
            name='AccountAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_discount', models.BooleanField(verbose_name=False)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
