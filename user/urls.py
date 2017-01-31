from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    url(r'^login', views.login_user, name='user_login'),

]