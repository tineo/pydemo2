from django.conf.urls import url
from banco.views import *

urlpatterns = [
    url(r'trans/$', view=TransaccionList.as_view(), name='trans'),
    url(r'transbycliente/$', view=TransaccionByCliente.as_view(), name='transbycliente'),
    url(r'transnew/$', view=TransaccionNew.as_view(), name='transnew'),
    url(r'bank/$', BancoList.as_view(), name='bank'),
    url(r'user/$', UsuarioList.as_view(), name='user'),
    url(r'account/$', CuentaList.as_view(), name='account'),
    url(r'account/(\d)/$', CuentaList.as_view(), name='account'),
    url(r'accountbynumber/$', CuentaNumber.as_view(), name='account'),
    url(r'login/$', Login.as_view(), name='login'),
]