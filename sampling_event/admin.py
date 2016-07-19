from django.contrib import admin

# Register your models here.

from .models import sampleEvent, sample, plate, Coge, Sampler, Site, Facility, Environment, Spacecraft

admin.site.register(sampleEvent)
admin.site.register(sample)
admin.site.register(plate)


admin.site.register(Coge)
admin.site.register(Sampler)
admin.site.register(Site)
admin.site.register(Facility)
admin.site.register(Environment)
admin.site.register(Spacecraft)
