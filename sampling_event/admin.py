from django.contrib import admin

# Register your models here.

from .models import sampleEvent, sample, plate, Coge, Sampler, Site, Environment, Spacecraft, Mission, JplUser

admin.site.register(sampleEvent)
admin.site.register(sample)
admin.site.register(plate)

admin.site.register(Mission)
#admin.site.register(Coge)
admin.site.register(Sampler)
admin.site.register(Site)
#admin.site.register(Facility)
admin.site.register(Environment)
admin.site.register(Spacecraft)
admin.site.register(JplUser)
