from django.contrib import admin
from .models import User, Classes, Group, GroupMember

# Register your models here.
admin.site.register(User)
admin.site.register(Classes)
admin.site.register(Group)
admin.site.register(GroupMember)