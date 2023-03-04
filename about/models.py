from django.db import models

from core.staging import upload_to
from core.utils import InfoModel, TimeStampBaseModel

# Create your models here.

class Header(TimeStampBaseModel, InfoModel):
    header_image_url = models.ImageField(upload_to=upload_to, blank=False, null=False)
    video_link_url = models.URLField(blank=False, null=False)

    def __str__(self):
        return str(self.title_Fr)


class AboutServices(TimeStampBaseModel, InfoModel):

    def __str__(self):
        return str(self.id)
    


class Achivement(TimeStampBaseModel):
    project_completed = models.IntegerField(default=0)
    satisfied_client = models.IntegerField(default=0)
    team_members = models.IntegerField(default=0)
    bands_joined = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.project_completed)
