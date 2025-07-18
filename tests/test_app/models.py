from django.db import models


class BehaveTestModel(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

    def get_absolute_url(self):
        return f'/behave/test/{self.number}/{self.name}'
