from .models import AboutServices, Header, Achivement
from rest_framework import serializers

class HeaderSerializer(serializers.ModelSerializer):
    header_image_url = serializers.ImageField(required=True)

    class Meta:
        model = Header
        fields = '__all__'


class AboutServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutServices
        fields = ['title', 'description']


class AchivementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achivement
        fields = '__all__'