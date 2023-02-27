from django.db import models


class TimeStampBaseModel(models.Model):
    created_at = models.DateTimeField(db_column='CreatedAt', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='UpdateAt', auto_now_add=True)

    class Meta:
        abstract = True


class InfoModel(models.Model):
    title = models.CharField(max_length=80, blank=False, null=False)
    description = models.TextField()
    
    class Meta:
        abstract = True