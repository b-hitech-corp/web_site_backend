from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import TimeStampBaseModel

# Create your models here.

class Contact(TimeStampBaseModel):
    name = models.CharField(max_length=80)
    company = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(_('email address'), db_index=True)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
