from django.db import models

from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class Services(TimeStampBaseModel, InfoModel):
    service_name = models.CharField(max_length=80, blank=False, null=False)
    service_image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.service_name