from __future__ import unicode_literals
import datetime
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from django.core.urlresolvers import reverse

from django.contrib.auth.models import AbstractBaseUser


class Mission(models.Model):
    missionName = models.CharField(max_length=50)

    def __str__(self):
        return str(self.missionName)


class Sampler(models.Model):
    mission = models.ForeignKey(Mission, default=1)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)


class Site(models.Model):
    #mission = models.ForeignKey(Mission, default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class SampleType(models.Model):
    method = models.CharField(max_length=10)
    efficiency = models.IntegerField()
    area = models.IntegerField()
    volume = models.DecimalField(max_digits=10, decimal_places=4 )
    platesCreated = models.IntegerField()

    def __str__(self):
        return str(self.method)


class Facility(models.Model):
    Site = models.ForeignKey(Site)
    name = models.CharField(max_length=100)

    def __str__(self):
         return str(self.name)


class Environment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Spacecraft(models.Model):
    mission = models.ForeignKey(Mission, default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Zone(models.Model):
    mission = models.ForeignKey(Mission, default=1)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.name)


class PooledID(models.Model):
    Zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Coge(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)

class sampleEvent(models.Model):

    mission = models.ForeignKey(Mission, default=1)
    date = models.DateField(default=datetime.date.today)
    assayName = models.CharField(max_length = 100)

    coge = models.CharField(max_length = 100) #eo
    samplers = models.ManyToManyField(Sampler)
    Site = models.ForeignKey(Site)
    facility = ChainedForeignKey(Facility, chained_field="Site", chained_model_field="Site", null=True, blank=True, default=None)
    #facility = models.CharField(max_length = 100) #eo
    environment = models.ForeignKey(Environment)



    def get_absolute_url(self):
    #    return "/sampling_event/{{self.id}}/"
        return reverse('sampling_event:detail', kwargs={'sampleEvent_id': self.id})

    def __str__(self):
        return self.assayName + '-' + str(self.id)
    #INCLUE PICTURES


class sample(models.Model):
    samplingEvent = models.ForeignKey(sampleEvent, on_delete=models.CASCADE)
    sampleType = models.ForeignKey(SampleType)
    accountable = models.BooleanField(default=True)

    Zone = models.ForeignKey(Zone, null=True, blank=True, default=None)
    PooledID = ChainedForeignKey(PooledID, chained_field="Zone", chained_model_field="Zone", null=True, blank=True, default=None)
    serialNumber = models.CharField(max_length=100, null=True, blank=True, default=None)
    description = models.CharField(max_length = 400, null=True, blank=True, default=None)

    #plates = models.IntegerField() - sampleType.platescreated

    #needs to be changed
    def get_absolute_url(self):
    #    return "/sampling_event/sample/{{self.id}}/"
        return reverse('sampling_event:sample-index', kwargs={'sample_id': self.id})

    def __str__(self):
        return str(self.sampleType) + '-' + str(self.id)


class plate(models.Model):
    sample = models.ForeignKey(sample, on_delete=models.CASCADE)

    #barcode = spacecraft - sampling event - sample - plate type - plate number
    #barcode = str(sample.samplingEvent) + str(sample.primary_key)

    sporeCount24 = models.CharField(max_length = 10)
    sporeCount48 = models.CharField(max_length = 10)
    sporeCount72 = models.CharField(max_length = 10)

    def __str__(self):
        return str(self.sampleID) + '-' + str(self.id)







