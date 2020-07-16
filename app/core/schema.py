from graphene import relay, ObjectType, List, Schema
from graphene_django import DjangoObjectType, DjangoConnectionField

from .models import Image, Property


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        interfaces = (relay.Node,)

class PropertyNode(DjangoObjectType):
    photos = List(ImageNode)

    def resolve_photos(self, info):
        return self.photos.all()

    class Meta:
        model = Property
        interfaces = (relay.Node, )



class Query(ObjectType):
    property = relay.Node.Field(PropertyNode)
    all_properties = DjangoConnectionField(PropertyNode)

schema = Schema(query=Query)
