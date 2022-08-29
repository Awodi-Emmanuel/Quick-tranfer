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
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model 

logger = logging.getLogger()
User = get_user_model()

class RegisterViewset(YkGenericViewSet):

    @swagger_auto_schema(
        operation_summary="signup",
        operation_description="Signup ",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        request_body=RegisterSerializer(),
    )
    
    @action(methods=["POST"], detail=False)
    
    def signup(self, request, *args, **kwargs):
        try:
                
            rcv_ser = RegisterSerializer(data=self.request.data)
            if rcv_ser.is_valid(raise_exception=True):
                password = rcv_ser.validated_data.pop('password', None)
                user = User.objects.create(**rcv_ser.validated_data)
                user.set_password(password)
                user.save()
                
                # return CreatedResponse({"message": "user created"})
                return GoodResponse()
            
        except Exception as e:
            logger.error(traceback.print_exc())
            return BadRequestResponse(str(e), code="unknown", request=self.request)