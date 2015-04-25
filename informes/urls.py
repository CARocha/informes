from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Tablero financiero SIMAS'

urlpatterns = [
    # Examples:
    # url(r'^$', 'informes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='user-login'),
    url(r'^', include('informesimas.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
