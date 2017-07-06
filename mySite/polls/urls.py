from django.conf.urls import url

from . import views,views_forms

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/your-name/
    url(r'^your-name/$', views_forms.get_name, name='your-name'),
    # ex: /polls/thanks/    
    url(r'^thanks/$', views_forms.show_thanks, name='thanks'),
]