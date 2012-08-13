from django.conf.urls.defaults import *

urlpatterns = patterns('comments.views',
	url(r'^load/([a-z]{1,10})/([\d]{1,10})/$', 		 'comments.load_comment', 		name='comments-post-comment'),
    url(r'^loadFrm/([\d]{1,10})/$',         'comments.load_form'),
    url(r'^post/$',          'comments.post_comment',       name='comments-post-comment'),
    url(r'^posted/$',        'comments.comment_done',       name='comments-comment-done'),
    url(r'^flag/(\d+)/$',    'moderation.flag',             name='comments-flag'),
    url(r'^flagged/$',       'moderation.flag_done',        name='comments-flag-done'),
    url(r'^delete/(\d+)/$',  'moderation.delete',           name='comments-delete'),
    url(r'^deleted/$',       'moderation.delete_done',      name='comments-delete-done'),
    url(r'^approve/(\d+)/$', 'moderation.approve',          name='comments-approve'),
    url(r'^approved/$',      'moderation.approve_done',     name='comments-approve-done'),
)

urlpatterns += patterns('',
    url(r'^cr/(\d+)/(.+)/$', 'django.contrib.contenttypes.views.shortcut', name='comments-url-redirect'),
)