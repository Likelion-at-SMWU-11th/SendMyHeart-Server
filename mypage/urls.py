from django.urls import path
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name = 'mypage'

urlpatterns = [
    path('profile/', my_profile_api, name='my_profile'),
    path('receiver/create/', create_receiver, name='create_receivers'),
    path('receiver/all/', get_receivers, name='receivers_all'),
    path('receiver/<int:receiver_id>/', receiver_detail_api, name='receiver_detail'),
    # 추가
    path('profile/<int:pk>/', my_profile_api, name='my_profile'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)