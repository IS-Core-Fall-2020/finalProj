from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return (self.user_name)
    
    class Meta:
        db_table = 'users'

class Classes(models.Model):

    class_description = models.CharField(max_length=100)

    def __str__(self) :
        return (self.class_description)

    class Meta :
        db_table = 'classes'

class Group(models.Model) :

    group_name = models.CharField(max_length=30)
    group_description = models.CharField(max_length=100)
    classes = models.ForeignKey(Classes, on_delete=models.PROTECT)

    def __str__(self) :
        return (self.group_name)

    class Meta :
        db_table = 'groups'

class GroupMember(models.Model):

    is_owner = models.BooleanField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) :
        return (self.user)

    class Meta :
        db_table = 'group_members'

class Assignment(models.Model) :

    assign_name = models.CharField(max_length=30)
    assign_description = models.CharField(max_length=250)
    assign_completion = models.BooleanField()
    assign_duedate = models.DateField(default=datetime.today, blank=True)
