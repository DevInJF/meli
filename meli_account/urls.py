from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

urlpatterns = [

    url(r'^add_account', views.add_account, name='meli_account_add'),
    url(r'^get_callback', views.get_callback, name='meli_account_get_callback'),
    url(r'^copy_account', views.copy_account, name='meli_account_copy'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]