from django.urls import path, include
from rest_framework import routers
from .views import VendorViewSet, PurchaseOrderViewSet, HistoricalPerformanceViewSet

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'historical_performances', HistoricalPerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
