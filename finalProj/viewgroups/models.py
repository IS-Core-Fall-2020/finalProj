from django.db import models
from django.apps import apps

#importing models from other apps
Classes = apps.get_model('viewclasses', 'Classes')
User = apps.get_model('loginpage', 'User')

# Create your models here.
class Group(models.Model):

    group_name = models.CharField(maxlength=30)
    group_description = models.CharField(maxlength=100)
    classes = models.ForeignKey(Classes, on_delete=models.PROTECT)

    def __str__(self) :
        return (self.group_name)

    class Meta:
        db_table = 'groups'

class GroupMember(models.Model):
    is_owner = models.BooleanField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) :
        return (self.user)

    class Meta:
        db_table = 'group_members'
