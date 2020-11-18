from django.db import models

# Create your models here.
class Group(models.Model):

    group_name = models.CharField(maxlength=30)
    group_description = models.CharField(maxlength=100)
    classID = models.ForeignKey(viewclasses, on_delete=models.DO_NOTHING)

    def __str__(self) :
        return (self.group_name)

    class Meta:
        db_table = 'groups'

class GroupMember(models.Model):
    is_owner = models.BooleanField()
    groupID = models.ForeignKey(viewgroups, on_delete=model.DO_NOTHING)
    personID = models.ForeignKey(loginpage, on_delete=model.DO_NOTHING)

    def __str__(self) :
        return (self.personID)

    class Meta:
        db_table = 'group_members'
