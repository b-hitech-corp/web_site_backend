from django.db import models
from django.utils.translation import gettext_lazy as _
from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class Member(TimeStampBaseModel, InfoModel):
    member_image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    member_name = models.CharField(max_length=80, blank=False, null=False)
    member_email = models.EmailField(_('email address'), db_index=True)
    member_phone = models.CharField(max_length=21, blank=False, null=False)
    occupation_Fr = models.CharField(max_length=80, blank=True, null=True)
    occupation_En = models.CharField(max_length=80, blank=True, null=True)
    experience_En = models.CharField(max_length=80, blank=True, null=True)
    experience_Fr = models.CharField(max_length=80, blank=True, null=True)
    bio_En = models.TextField(blank=True, null=True)
    bio_Fr = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member_name}-({self.member_email}-({self.occupation_Fr})"
    

class Header(TimeStampBaseModel):
    header_image_url = models.ImageField(upload_to=upload_to, blank=False, null=False)
    title_Fr = models.CharField(max_length=80, blank=True, null=True)
    title_En = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return str(self.title_Fr)