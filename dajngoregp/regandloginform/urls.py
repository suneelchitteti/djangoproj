from django.conf.urls import url
from . import views
app_name='regandloginform'
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^reg$',views.reg,name='reg'),
    url(r'login$',views.login,name='login')
]