from django.db import models
from core import settings
from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class FeedBack(TimeStampBaseModel, InfoModel):
    customer_image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    customer_name = models.CharField(max_length=80, blank=False, null=False)
    occupation_Fr = models.CharField(max_length=80, blank=False, null=False)
    occupation_En = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return f"{self.customer_name}-({self.occupation_Fr}-({self.title_Fr})"
    

class Header(TimeStampBaseModel):
    header_image_url = models.ImageField(upload_to=upload_to, blank=False, null=False)
    title_Fr = models.CharField(max_length=80, blank=False, null=False)
    title_En = models.CharField(max_length=80, blank=False, null=False)
    section_title_Fr = models.CharField(max_length=80, blank=False, null=False)
    section_title_En = models.CharField(max_length=80, blank=False, null=False)
    section_description_Fr = models.TextField(blank=True, null=True)
    section_description_En = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title_Fr)
