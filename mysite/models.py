from django.db import models

class SensorData(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    value = models.FloatField()
    rectime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-rectime',)

    def __str__(self):
        return self.name
