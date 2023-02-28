from core.utils import Base64ImageField
from .models import FeedBack, Header
from rest_framework import serializers

class FeedBackSerializer(serializers.ModelSerializer):
    customer_image_url = serializers.ImageField(required=True)

    class Meta:
        model = FeedBack
        fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):
    header_image_url = serializers.ImageField(required=True)
    # header_image_url = Base64ImageField(required=True, max_length=None, use_url=False, allow_empty_file=True, allow_null=True, ),

    class Meta:
        model = Header
        fields = '__all__'
