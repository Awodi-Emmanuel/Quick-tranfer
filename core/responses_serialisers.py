from rest_framework.serializers import Serializer, CharField, IntegerField, JSONField

class EmptySerializer(Serializer):
    class Meta:
        ref_name = None
        
class BadRequestResponseSerializer(Serializer):
    message = CharField()
    code = CharField()
    data = JSONField()
    
    class Meta:
        ref_name = None
        
        
        
class NotFoundResponseSerializer(Serializer):
    message = CharField()
    model = CharField()
    data = JSONField()
    
    class Meta: 
        ref_name = None
        
        
