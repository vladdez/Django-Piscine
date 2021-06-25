from django.urls import path, include
from .views import HomePageView, ImageFormViev
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_image/', ImageFormViev.as_view(), name='add_image'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)