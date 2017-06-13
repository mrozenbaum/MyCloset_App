from django.conf.urls import url
from . import views

# app_name = "myclosetapp"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^my_categories$', views.my_categories, name='mycategories'),
]