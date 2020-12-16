from django.contrib import admin
from .models import Sensor,Home,ContactPSP
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display=('home_add','name')

admin.site.register(Home,HomeAdmin)

class SensorAdmin(admin.ModelAdmin):
    list_display=('name','home_add','area','type')

admin.site.register(Sensor,SensorAdmin)


class PSPAdmin(admin.ModelAdmin):
    list_display=('type','contact')

admin.site.register(ContactPSP,PSPAdmin)
