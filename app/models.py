from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    register_status = (
        ('approve', 'approve'),
        ('pending', 'pending'),
        ('reject', 'reject'),
    )
    phone_number = models.CharField(max_length=10)
    user_type = models.CharField(max_length=100)
    status = models.CharField(choices=register_status, default='pending', max_length=50)

class Package(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    img1 = models.FileField(upload_to='package')
    img2 = models.FileField(upload_to='package')
    expiry_date = models.DateField()
    price = models.IntegerField()
    no_of_days = models.IntegerField()
    no_of_night = models.IntegerField()
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.expiry_date
    
    def __str__(self):
        return self.package_name + ' created by ' + self.user_id.username
    
class HealthAssistant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    qualification = models.CharField(max_length=200)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} ({self.qualification})"


class Booking(models.Model):
    booking_status = (
        ('booked', 'booked'),
        ('pending', 'pending'),
        ('reject', 'reject'),
        ('paid', 'paid'),
        ('approved', 'approved')
    )
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    no_of_people = models.IntegerField()
    booking_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    HealthAssistant_id = models.ForeignKey(HealthAssistant, on_delete=models.CASCADE,null=True)
    status = models.CharField(choices=booking_status, default='pending', max_length=50)
    total_amount = models.IntegerField()
    rating = models.IntegerField(null=True, blank=True)
    review = models.CharField(max_length=200, null=True, blank=True)







