from django.contrib import admin

# Register your models here.

from .models import sampleEvent, sample, plate

admin.site.register(sampleEvent)
admin.site.register(sample)
admin.site.register(plate)