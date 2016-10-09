from django.conf.urls import url
from formation import views

urlpatterns = [
    url(r'^formateurs/$', views.formateur_list),
    #url(r'^formateurs/(?P<pk>[0-9]+)/$', views.formateur_detail),
]
