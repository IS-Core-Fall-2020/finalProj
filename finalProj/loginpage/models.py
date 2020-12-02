from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User

'''
from django.db.models.signals import post_save
from django.dispatch import receiver
'''
# Create your models here.
'''
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
'''
'''
#user profile test extend
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
class Classes(models.Model):

    class_description = models.CharField(max_length=100)

    def __str__(self) :
        return (self.class_description)

    class Meta :
        db_table = 'classes'

'''
class GroupMember(models.Model):

    is_owner = models.BooleanField()
    user = models.ManyToManyField(User)

    def __str__(self) :
        return (self.user)

    class Meta :
        db_table = 'group_members'
'''

class Group(models.Model) :

    group_name = models.CharField(max_length=30)
    group_description = models.CharField(max_length=100)
    classes = models.ManyToManyField(Classes)
    #group_member = models.OneToOneField(GroupMember, on_delete=models.PROTECT)
    user = models.ManyToManyField(User)

    def __str__(self) :
        return (self.group_name)

    class Meta :
        db_table = 'groups'







class Assignment(models.Model) :

    assign_name = models.CharField(max_length=30)
    assign_description = models.CharField(max_length=250)
    assign_completion = models.BooleanField()
    assign_duedate = models.DateField(default=datetime.today, blank=True)
