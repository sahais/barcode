from __future__ import unicode_literals
import datetime
from django.db import models
from django.core.urlresolvers import reverse


class sampleEvent(models.Model):
    date = models.DateField(default=datetime.date.today)
    assayName = models.CharField(max_length = 100)
    coge = models.CharField(max_length = 100)
    samplers = models.CharField(max_length = 300)
    site = models.CharField(max_length = 100)
    facility = models.CharField(max_length = 100)
    environment = models.CharField(max_length = 100)
    spacecraft = models.CharField(max_length=100)

    #wipeNum = models.PositiveIntegerField
    #swabNum = models.PositiveIntegerField
    #airNum = models.PositiveIntegerField

    #otherNum = models.PositiveIntegerField
    #mediaControlNum = models.PositiveIntegerField
    #positiveControlNum = models.PositiveIntegerField


    def get_absolute_url(self):
    #    return "/sampling_event/{{self.id}}/"
        return reverse('sampling_event:detail', kwargs={'sampleEvent_id': self.id})

    def __str__(self):
        return self.assayName + '-' + str(self.id)
    #INCLUE PICTURES


class sample(models.Model):
    samplingEvent = models.ForeignKey(sampleEvent, on_delete=models.CASCADE)

    SAMPLE_CHOICES = (
        ("a", "air"),
        ("s", "swab"),
        ("w", "wipe"),
        ("o", "other"),
        ("pc", "positive-control"),
        ("mc", "media-control"),

    )
    sampleType = models.CharField(max_length=2, choices=SAMPLE_CHOICES)

    zoneID = models.CharField(max_length=100)
    subCategory = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    serialNumber = models.CharField(max_length=100)
    accountable = models.BooleanField(default = True)
    description = models.CharField(max_length = 400)

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
        return str(self.sample) + '-' + str(self.id)


class SampleType(models.Model):
    method = models.CharField(max_length=10)
    efficiency = models.IntegerField()
    area = models.IntegerField()
    volume = models.DecimalField(max_digits=10, decimal_places=4 )
    platesCreated = models.IntegerField()

    def __str__(self):
        return str(self.method)


class Coge(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)


class Sampler(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.firstName) + ' ' + str(self.lastName)


class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Facility(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Environment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Spacecraft(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)











