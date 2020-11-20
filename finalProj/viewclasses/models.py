from django.db import models

# Create your models here.

class Class(models.Model):
    group_description = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    classID = models.ForeignKey(viewclasses, on_delete=models.PROTECT)
    groupID = models.ForeignKey(viewgroups, on_delete=models.PROTECT)

    def __str__(self) :
        return (self.group_description)   

    class Meta:
        db_table = 'classes'