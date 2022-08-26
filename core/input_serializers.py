from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer, ValidationError
from django.core.validators import validate_email as dj_validate_email
from django.db.models import Q
from django.utils.translation import gettext as _ 
from rest_framework.fields import *



User = get_user_model()

class RegisterSerializer(Serializer):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    
    class Meta:
        ref_name = None
    
    