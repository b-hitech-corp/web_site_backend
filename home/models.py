from django.db import models

from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class FeedBack(TimeStampBaseModel, InfoModel):
    customer_image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    customer_name = models.CharField(max_length=80, blank=False, null=False)
    occupation = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return f"{self.customer_name}-({self.occupation}-({self.title})"
    

class Header(TimeStampBaseModel):
    header_image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    title = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.title