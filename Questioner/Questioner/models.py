from django.db import models
from datetime import datetime

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
       abstract = True


class User(Base):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return "{}".format(self.name)

class Question(Base):
    title = models.TextField()
    user = models.ForeignKey(User)
    private = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}".format(self.title)
   
class Answer(Base):
    body = models.TextField()
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return "{}".format(self.body)

class Tenant(Base):
    name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100)

    def __unicode__(self):
        return "Name: {} | Api Key: {}".format(self.name, self.api_key)

class TApiCount(Base):
    tenant = models.ForeignKey(Tenant)
    request_count = models.IntegerField(default=0)
    next_request_time = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return "Tenant: {} | Api Request Count: {} | created: {}".format(self.tenant.name, self.request_count, self.created)