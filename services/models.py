from django.db import models
from tinymce.models import HTMLField

from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class Services(TimeStampBaseModel, InfoModel):
    service_name_Fr = models.CharField(max_length=80, blank=False, null=False)
    service_name_En = models.CharField(max_length=80, blank=False, null=False)
    service_image_url = models.ImageField(upload_to=upload_to, blank=False, null=False)
    description_En = HTMLField()
    description_Fr = HTMLField()

    def __str__(self):
        return str(self.service_name_Fr)
