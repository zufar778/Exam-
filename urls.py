from django.urls import path
from .views import Login_views, Registration_views, Logout_views, Index_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Index_views, name='index'),
    path('register/', Registration_views, name='register'),
    path('login/', Login_views, name='login'),
    path('logout/', Logout_views, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


