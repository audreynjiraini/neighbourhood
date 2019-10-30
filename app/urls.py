from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search_results, name='search'),
    url(r'^business$', views.business, name='business'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^profile/(?P<username>\w{0,50})$', views.profile, name='profile'),
    url(r'^profile/edit/(?P<username>\w{0,50})$', views.edit_profile, name='edit_profile'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^business/new/$', views.new_business, name='new_business')
]