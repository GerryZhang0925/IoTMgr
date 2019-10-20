from django.conf.urls import url
from DevMgr import views

# template urls
app_name = 'DevMgr'

urlpatterns = [
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^plant_list/$', views.plant_list, name='plant_list'),
    url(r'^data_list/$', views.data_list, name='data_list'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
