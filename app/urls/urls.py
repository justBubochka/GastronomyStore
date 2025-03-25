from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views.admin_panel.views_admin_panel import ProductViewSet, ProductListView, ProductDetailsView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin_panel/', ProductListView.as_view(), name='admin_products_list'),
    path('admin_panel/product/<int:pk>/', ProductDetailsView.as_view(), name='admin_product_details')
]