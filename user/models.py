from django.db import models

class MassSpectro(models.Model):
    sample_names = models.CharField(max_length= 30, blank = False)
    counts = models.IntegerField()
    files = models.FileField(upload_to = 'Spectrs/%Y/%m/%d/')
    table = models.FileField(upload_to = 'Table/%Y/%m/%d/')
    data = models.DateField()