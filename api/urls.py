# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import VendorViewSet, PurchaseOrderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = SimpleRouter()
router.register(
    r'vendors',
    VendorViewSet,
    basename='vendor'
)
router.register(
    r'purchase_orders',
    PurchaseOrderViewSet,
    basename='purchaseorder'
)
# router.register(
#     r'users',
#     UserViwSets,
#     basename='users'

# )
urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += router.urls
