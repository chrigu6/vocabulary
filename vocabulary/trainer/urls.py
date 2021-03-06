from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registerUser$', views.register_user, name='register_user'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^populate$', views.populate_words, name='populate'),
    url(r'^upload_success$', views.upload_success, name='upload_success'),
]