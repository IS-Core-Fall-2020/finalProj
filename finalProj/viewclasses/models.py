from django.db import models
from django.apps import apps

#importing models from other apps
Group = apps.get_model('viewgroups', 'Group')

# Create your models here.

class Classes(models.Model):
    group_description = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self) :
        return (self.group_description)   

    class Meta:
        db_table = 'classes'