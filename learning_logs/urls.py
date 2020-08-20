"""Defines URL patterns for learning_logs"""
from django.conf.urls import url
from django.urls import include, path
from . import views

#Adding this when it is bring NoReverseMatch: Learning
app_name = 'learning_logs'

urlpatterns = [

    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # page for adding new entry
    #Note url is not working for pattern that has <int:topic_id>, you need to change it to path.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # page for adding a new topic
    url('new_topic/$', views.new_topic, name='new_topic'),

    # for individual topic r'^topics/(?P<topic_id>\d+
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Note: the index url pattern should be shifted to come
    # after all other url pages because it overide any url after it
    # show all topics
    url('topics/', views.topics, name='topics'),

    #Home page
    url('', views.index, name='index'),



]