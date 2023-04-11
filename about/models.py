from django.db import models
from tinymce.models import HTMLField

from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class Header(TimeStampBaseModel, InfoModel):
    header_image_url = models.ImageField(upload_to=upload_to, blank=False, null=False)
    video_link_url = models.URLField(blank=False, null=False)
    second_title_Fr = models.CharField(max_length=80, blank=True, null=True)
    second_description_Fr = models.TextField(blank=True, null=True)
    second_title_En = models.CharField(max_length=80, blank=True, null=True)
    second_description_En = models.TextField(blank=True, null=True)
    second_image = models.ImageField(upload_to=upload_to, blank=False, null=False)

    def __str__(self):
        return str(self.title_Fr)


class AboutServices(TimeStampBaseModel, InfoModel):
    description_En = HTMLField()
    description_Fr = HTMLField()

    def __str__(self):
        return str(self.id)
    


class HistoryAndMission(TimeStampBaseModel):
    history_Fr = models.CharField(max_length=80, blank=True, null=True)
    history_description_Fr = models.TextField(blank=True, null=True)
    history_En = models.CharField(max_length=80, blank=True, null=True)
    history_description_En = models.TextField(blank=True, null=True)
    mission_Fr = models.CharField(max_length=80, blank=True, null=True)
    mission_description_Fr = models.TextField(blank=True, null=True)
    mission_En = models.CharField(max_length=80, blank=True, null=True)
    mission_description_En = models.TextField(blank=True, null=True)
    vision_Fr = models.CharField(max_length=80, blank=True, null=True)
    vision_description_Fr = models.TextField(blank=True, null=True)
    vision_En = models.CharField(max_length=80, blank=True, null=True)
    vision_description_En = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.history_Fr)
    


class Achivement(TimeStampBaseModel):
    project_completed = models.IntegerField(default=0)
    satisfied_client = models.IntegerField(default=0)
    team_members = models.IntegerField(default=0)
    bands_joined = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.project_completed)
