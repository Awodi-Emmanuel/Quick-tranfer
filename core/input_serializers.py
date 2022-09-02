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
    username = CharField()
    class Meta:
        ref_name = None
    
    
class TranserSerializer(Serializer):
    account_balance = CharField()
    username = CharField()
    
    class Meta:
        ref_name = None
        
class SigninInputSerializer(Serializer):
    email = EmailField(required=False, allow_null=True)
    username = CharField(required=False, allow_null=True)
    password = CharField()

    class Meta:
        ref_name = None

    def validate_password(self, *args):
        username = self.initial_data.get("username")
        email = self.initial_data.get("email")
        password = self.initial_data.get("password")

        if not email and not username:
            raise ValidationError(_("(username or email) fields should be present."))

        return password