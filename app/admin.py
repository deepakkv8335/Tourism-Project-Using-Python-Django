from django.contrib import admin
from .models import CustomUser, Package, Booking, HealthAssistant
from django.contrib.auth.models import Group

class UserDetails(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["username", "user_type","status"]}),
        ("More information", {"fields": ["phone_number", "email"]}),
    ]

    list_display = ["username", "user_type", "status"]    
    list_filter = ["user_type", "status"]                           
    search_fields = ["username"]                                   
    list_per_page = 10 


class PackageDetails(admin.ModelAdmin):
    list_display = ["user_username", "package_name", "destination","expiry_date","is_active"]
    list_filter = ["price", "no_of_days","is_active" ]
    search_fields = ["user_id__username", "package_name"]  
    list_per_page = 10

    def user_username(self, obj):
        return obj.user_id.username


    user_username.short_description = "Username"




class BookingDetails(admin.ModelAdmin):
    list_display = ["user_username", "package_name", "agency_name", "status"]
    list_filter = ["status"]
    search_fields = ["user_id__username", "package_id__package_name"]  
    list_per_page = 10

    def user_username(self, obj):
        return obj.user_id.username

    def package_name(self, obj):
        return obj.package_id.package_name
    
    def agency_name(self, obj):
        return obj.package_id.user_id.username

    user_username.short_description = "Username"
    package_name.short_description = "Package Name"
    agency_name.short_description = "Agency Name"



admin.site.register(CustomUser, UserDetails)
admin.site.register(Package, PackageDetails)
admin.site.register(Booking, BookingDetails)
admin.site.register(HealthAssistant)

admin.site.unregister(Group)
admin.site.site_header = 'ADMIN PANNEL'