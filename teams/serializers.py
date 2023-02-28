from .models import Member, Header
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    member_image_url = serializers.ImageField(required=True)

    class Meta:
        model = Member
        fields = '__all__'



class HeaderSerializer(serializers.ModelSerializer):
    header_image_url = serializers.ImageField(required=True)

    class Meta:
        model = Header
        fields = '__all__'