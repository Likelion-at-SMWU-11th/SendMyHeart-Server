from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/additional_info/', views.additional_info, name='additional_info'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)