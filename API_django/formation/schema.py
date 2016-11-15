from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from formation.models import Formateur, Stage

class FormateurNode(DjangoObjectType):
    class Meta:
        model = Formateur
        filter_fields = ['nom', 'prenom', 'contact']
        filter_order_by = ['nom']
        interfaces = (relay.Node, )

class Query(AbstractType):
    formateur = relay.Node.Field(FormateurNode)
    all_formateurs = DjangoFilterConnectionField(FormateurNode)
