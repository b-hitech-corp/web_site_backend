from .models import Services
from .serializers import ServicesSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class ServicesViewSet(ModelViewSet):
    serializer_class = ServicesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Services.objects.order_by('service_name_Fr')
