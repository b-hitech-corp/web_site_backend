from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from teams.views import *
from home.views import *
from about.views import *
from services.views import *
from contact.views import ContactViewSet


router = routers.DefaultRouter()


router.register('home', HomeHeaderViewSet, basename='header')
router.register('home-feedback', FeedBackViewSet, basename='feedback')

router.register('teams-member', MemberViewSet, basename='member')

router.register('about', AboutHeaderViewSet, basename='about-header')
router.register('about-achivement', AchivementViewSet, basename='achivement')
router.register('about-mission', HistoryAndMissionViewSet, basename='missions-history')
router.register('about-services', AboutServicesViewSet, basename='about-services')

router.register('services', ServicesViewSet, basename='services')
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/', include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
