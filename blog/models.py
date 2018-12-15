import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __repr__(self):
        return "Post(title={}, body={}, pub_date={}".format(
            self.title,
            self.body,
            self.pub_date
        )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

