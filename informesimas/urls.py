from django.conf.urls import include, url
from .views import index_view, consultar

urlpatterns = [

    url(r'^$', consultar, name='consultar'),
    url(r'^tablero/$', index_view, name='index'),
]