from django.urls import re_path as url

from slack_utils import views

urlpatterns = [
    url('events/$', views.EventsView.as_view(), name='slack-events-api'),
    url('commands/$', views.CommandView.as_view(), name='slack-commands'),
]
