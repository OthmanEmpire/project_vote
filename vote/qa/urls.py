from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.splash, name='splash'),
    re_path(r'^voting$', views.voting, name='voting'),
    re_path(r'^postQuestion$', views.postQuestion, name='postQuestion'),
    re_path(r'^about$', views.about, name='about'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
