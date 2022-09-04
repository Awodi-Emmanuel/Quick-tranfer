# from asyncio.log import logger
import logging
import traceback
from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
)
from core.custom_classes import YkGenericViewSet
from core.custom_classes import YkGenericViewSet
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from core.input_serializers import RegisterSerializer 
from core.model_serializer import UserSerializer
from .input_serializers import SigninInputSerializer
from .responses_serialisers import (
    EmptySerializer,
    NotFoundResponseSerializer,
    BadRequestResponseSerializer,
    
)
from .responses import (
    BadRequestResponse,
    CreatedResponse,
    GoodResponse,
    
)

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model 
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework import status

logger = logging.getLogger()
User = get_user_model()

class AuthViewset(YkGenericViewSet):

    @swagger_auto_schema(
        operation_summary="signup",
        operation_description="Signup ",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        request_body=UserSerializer(),
    )
    
    @action(methods=["POST"], detail=False, authentication_classes = (), permission_classes = ())
    
    def signup(self, request, *args, **kwargs):
        try:
                
            rcv_ser = UserSerializer(data=self.request.data)
            if rcv_ser.is_valid(raise_exception=True):
                rcv_ser.save()
                
                return GoodResponse(rcv_ser.data)
                #return CreatedResponse({"message": "user created"})
            
        except Exception as e:
            logger.error(traceback.print_exc())
            return BadRequestResponse(str(e), code="unknown", request=self.request)
        
        
    @swagger_auto_schema(
        operation_summary="login",
        operation_description="login",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        # request_body=UserSerializer(),
        
    )
    
    @action(methods=["POST"], detail=False, permission_classes = ())
        
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                return GoodResponse({"token": user.auth_token.key, "username": username})
            else:
                return Response(
                    {"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            traceback.print_exc()
            return BadRequestResponse(str(e), "Unknown", request=self.request)
        

 
            
 