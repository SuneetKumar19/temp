from django.conf.urls import url 
from basic_app import views


#For Template tagging  here variable needs to be specifically named as app_name
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$',views.relative ,name="relative"),
    url(r'^other/$',views.other,name='other'),
]



