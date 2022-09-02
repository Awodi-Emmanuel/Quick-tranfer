from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .api_views import (
#     RegisterViewset,
#     BalanceViewset,
#     # TransferViewset
#     )


router = DefaultRouter()
# router.register("manage-tranfer", BalanceViewset, basename="balance-api")
# router.register('tranfer', TransferViewset, basename='transfer')
# router.register('register', RegisterViewset, basename='rigster')
# router.register('manage-tranfer', BalanceViewset, basename='transfer')




urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', TokenRefreshView.as_view())
    
    
]

urlpatterns += router.urls