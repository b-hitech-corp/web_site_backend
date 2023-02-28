from .models import AboutServices, Header
from .serializers import AboutServicesSerializer, HeaderSerializer, AchivementSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class AboutHeaderViewSet(ModelViewSet):
    serializer_class = HeaderSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Header.objects.order_by('title_Fr')



class AboutServicesViewSet(ModelViewSet):
    serializer_class = AboutServicesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AboutServices.objects.order_by('title_Fr')
    


class AchivementViewSet(ModelViewSet):
    serializer_class = AchivementSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AboutServices.objects.all()