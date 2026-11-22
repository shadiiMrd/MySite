from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', include('main.urls'), name='main'),
                   path('about/', include('about.urls'), name='about'),
                   path('project/', include('project.urls'), name='project'),
                   path('contact/', include('contact.urls'), name='contact'),
                   path('experience/', include('experience.urls'), name='experience'),

               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
