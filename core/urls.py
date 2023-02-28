from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from teams.views import TeamsHeaderViewSet, MemberViewSet
from home.views import FeedBackViewSet, HomeHeaderViewSet
from about.views import *
from services.views import ServicesViewSet
from contact.views import ContactViewSet


router = routers.DefaultRouter()


router.register('home', HomeHeaderViewSet, basename='header')
router.register('home/feedback', FeedBackViewSet, basename='feedback')

router.register('teams', TeamsHeaderViewSet, basename='team-header')
router.register('teams/member', MemberViewSet, basename='member')

router.register('about', AboutHeaderViewSet, basename='about-header')
router.register('about/achivement', AchivementViewSet, basename='achivement')
router.register('about/services', AboutServicesViewSet, basename='about-services')

router.register('services', ServicesViewSet, basename='services')
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)