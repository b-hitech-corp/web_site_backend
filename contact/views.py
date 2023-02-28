from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from contact.models import Contact
from contact.serializers import ContactSerializer
from core.utils import Util
from rest_framework.response import Response
from decouple import config


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Contact.objects.order_by('name')
    
    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_email = serializer.data['email']
            user_name = serializer.data['name']
            user_subject = serializer.data['subject']
            user_message = serializer.data['message']
            user_company = serializer.data['company']
        email_body = 'Salut '+user_name.upper()+'\nNous vous informons que votre demande est en cours de traitement.\nMerci'
        data_for_user = {'email_subject': "Confirmation de soumission", 'email_body': email_body, 'from': config('EMAIL_HOST_USER'), 'to_email': user_email}
        Util.send_email(data_for_user)
        data_for_bht = {'email_subject': user_subject+' de '+user_company, 'email_body': user_message, 'from': user_email, 'to_email': config('EMAIL_HOST_USER')}
        Util.send_email(data_for_bht)
        return Response(serializer.data)