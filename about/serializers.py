from .models import AboutServices, Header, Achievement
from rest_framework import serializers

class HeaderSerializer(serializers.ModelSerializer):
    header_image_url = serializers.ImageField(required=True)

    class Meta:
        model = Header
        fields = ['video_link_url', 'header_image_url', 'title', 'description']



class AboutServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutServices
        fields = ['title', 'description']



class AchivementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = '__all__'