from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('chat/', include('chat.urls')),
    path('discussions/', include('discussions.urls')),
    path('movies/', include('movies.urls')),
    path('select2/', include('django_select2.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
