from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from home.views import FeedBackViewSet, HeaderViewSet
from about.views import AboutServicesViewSet, AchivementSerializer, HeaderSerializer
from services.views import ServicesViewSet
from contact.views import ContactViewSet

router = routers.SimpleRouter()

router.register('home', HeaderViewSet, basename='header')
router.register('home/feedback', FeedBackViewSet, basename='feedback')

router.register('about', HeaderSerializer, basename='header')
router.register('about/achivement', AchivementSerializer, basename='achivement')
router.register('about/services', AboutServicesViewSet, basename='about-services')

router.register('services', ServicesViewSet, basename='services')
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('router.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)