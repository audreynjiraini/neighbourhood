from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search_results, name='search'),
    url(r'^business$', views.business, name='business'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^profile/(?P<username>\w{0,50})$', views.profile, name='profile'),
]