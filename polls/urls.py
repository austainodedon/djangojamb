# 1 Generic views are normally used from the beginning
# and they help you avoid having to write a lot
# of custom code

from django.conf.urls import url

from . import views

app_name = 'polls'

# 1 We'll change the urlpatterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
