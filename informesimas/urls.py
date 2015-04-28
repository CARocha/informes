from django.conf.urls import include, url
from .views import index_view, consultar

urlpatterns = [

    url(r'^$', consultar, name='consultar'),
]