from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myclosetapp/', include('myclosetapp.urls', namespace="myclosetapp")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

