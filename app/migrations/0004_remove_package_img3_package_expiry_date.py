# Generated by Django 5.0.6 on 2024-05-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_booking_rating_alter_booking_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='img3',
        ),
        migrations.AddField(
            model_name='package',
            name='expiry_date',
            field=models.DateTimeField(default='2024-12-31'),
            preserve_default=False,
        ),
    ]