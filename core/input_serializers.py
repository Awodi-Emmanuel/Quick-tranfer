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
    password = CharField()
    
    class Meta:
        ref_name = None
        
        
    
    def validate_username(self, *args):
        username = self.initial_data["username"]
        u = User.objects.filter(username=username).first()
        if u: 
        #and u.date_joined >= datetime(2020, 1, 1, tzinfo=pytz.UTC):
            raise ValidationError("Username is already used.")
        return username

    def validate_email(self, *args):
        email = self.initial_data["email"]
        try:
            dj_validate_email(email)
            user = User.objects.filter(email=email).first()
            if user: 
            # and user.date_joined >= datetime(2020, 1, 1, tzinfo=pytz.UTC):
                raise ValidationError("This email already used")
        except ValidationError as e:
            raise e

        return email

    # def create_user(self):
    #     username = self.validated_data["username"]
    #     email = self.validated_data["email"]
    #     first_name = self.validated_data["first_name"]
    #     last_name = self.validated_data["last_name"]
    #     password = self.validated_data["password"]

    #     user = User.objects.filter(email=email).first()
    #     return user
    
    
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
        # email = self.initial_data.get("email")
        password = self.initial_data.get("password")

        if  not username:
            raise ValidationError(_("(username) fields should be present."))

        return password