from django.db import models

class Discipline(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return 'discipline-' + str(self.id)

class Industry(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return 'industry-' + str(self.id)