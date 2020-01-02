from django.conf.urls import url

from .views import (
    create_moderator,
    moderator_detail,
    update_moderator,
    delete_moderator,
    moderator_list,

    hide_thread,
    unhide_thread,
)

urlpatterns = [
    url(r'^add/$', create_moderator, name='moderator_create'),
    url(
        r'^(?P<username>[\w-]+)/detail/$', moderator_detail, name='moderator_detail'
    ),
    url(
        r'^(?P<username>[\w-]+)/edit/$', update_moderator, name='moderator_update'
    ),
    url(
        r'^(?P<username>[\w-]+)/delete/$', delete_moderator, name='moderator_delete'
    ),
    url(r'^list/$', moderator_list, name='moderator_list'),

    url(r'^threads/(?P<slug>[\w-]+)/hide/$', hide_thread, name='thread_hide'),
    url(r'^threads/(?P<slug>[\w-]+)/unhide/$', unhide_thread, name='thread_unhide'),

]

