from django.contrib.auth.models import User
from django.db import models

class Screenshot(models.Model):
    raw = models.ImageField(upload_to='raw_screens/%Y/%m/%d', default='no-image.png')
    upload_date = models.DateTimeField()
    user = models.ForeignKey(User)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.raw.name)

