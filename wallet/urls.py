from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import WalletViewset 


router = DefaultRouter()
router.register("trans", WalletViewset, basename="trans")




urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', TokenRefreshView.as_view())
    
    
]

urlpatterns += router.urls