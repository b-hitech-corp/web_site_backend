from django.db import models
from django.core.mail import EmailMessage
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

class TimeStampBaseModel(models.Model):
    created_at = models.DateTimeField(db_column='CreatedAt', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='UpdateAt', auto_now_add=True)

    class Meta:
        abstract = True


class InfoModel(models.Model):
    title_Fr = models.CharField(max_length=80, blank=True, null=True)
    description_Fr = models.TextField(blank=True, null=True)
    title_En = models.CharField(max_length=80, blank=True, null=True)
    description_En = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject = data['email_subject'], body = data['email_body'],from_email = data['from'] , to = [data['to_email']])
        email.send()


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
        
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension