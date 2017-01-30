from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    url(r'^$', views.index, name='jobs_list'),

]