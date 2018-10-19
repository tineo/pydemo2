from django.conf.urls import url
from banco.views import *

urlpatterns = [
    url(r'trans/$', TransaccionList.as_view(), name='trans'),
    url(r'bank/$', BancoList.as_view(), name='bank'),
    url(r'user/$', UsuarioList.as_view(), name='user'),
    url(r'account/$', CuentaList.as_view(), name='account'),
]