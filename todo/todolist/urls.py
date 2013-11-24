from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from todolist.models import Todo

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Mongo ID regex
mid = '(?P<id>[0-9a-f]{24})'

urlpatterns = patterns('todolist.views',
  url(r'^$',ListView.as_view(
    queryset=Todo.objects.order_by('created'),
    context_object_name='todos',
    template_name = 'todolist/index.html'
  )),
  url(r'^create','create'),
  url(r'^'+mid+r'/delete','delete'),
  url(r'^'+mid+r'/edit','edit'),
)
