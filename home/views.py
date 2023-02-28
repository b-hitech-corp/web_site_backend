from .models import FeedBack, Header
from .serializers import FeedBackSerializer, HeaderSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class FeedBackViewSet(ModelViewSet):
    serializer_class = FeedBackSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return FeedBack.objects.order_by('customer_name')
    

class HomeHeaderViewSet(ModelViewSet):
    serializer_class = HeaderSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Header.objects.order_by('title_Fr')
