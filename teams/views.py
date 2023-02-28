from .models import Member, Header
from .serializers import MemberSerializer, HeaderSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Member.objects.order_by('member_name')
    

class TeamsHeaderViewSet(ModelViewSet):
    serializer_class = HeaderSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Header.objects.order_by('title_Fr')
