from django.contrib import admin

# Register your models here.

from .models import sampleEvent, sample, plate, Sampler, Coge, Site, Environment, Facility, Spacecraft, Mission, Zone, PooledID, SampleType

admin.site.register(sampleEvent)
admin.site.register(sample)
admin.site.register(plate)

admin.site.register(Mission)
admin.site.register(Coge)
admin.site.register(Sampler)
admin.site.register(Site)
admin.site.register(Environment)

#admin.site.register(Spacecraft)
admin.site.register(Facility)
admin.site.register(Zone)
admin.site.register(PooledID)
admin.site.register(SampleType)

#admin.site.register(Facility)