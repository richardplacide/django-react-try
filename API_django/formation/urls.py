from django.conf.urls import url
from graphene_django.views import GraphQLView
from formation import views


urlpatterns = [
    url(r'^formateurs/$', views.formateur_list),
    url(r'^stages/$', views.stage_list),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    #url(r'^formateurs/(?P<pk>[0-9]+)/$', views.formateur_detail),
]
