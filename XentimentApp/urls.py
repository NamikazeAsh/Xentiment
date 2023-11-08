from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from XentimentApp import views

urlpatterns = [
    path('',views.XentimentHome,name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)