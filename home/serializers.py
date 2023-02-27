from .models import FeedBack, Header
from rest_framework import serializers

class FeedBackSerializer(serializers.ModelSerializer):
    customer_image_url = serializers.ImageField(required=True)

    class Meta:
        model = FeedBack
        fields = ['customer_name', 'occupation', 'customer_image_url', 'title', 'description']


class HeaderSerializer(serializers.ModelSerializer):
    header_image_url = serializers.ImageField(required=True)

    class Meta:
        model = Header
        fields = ['header_image_url', 'title']