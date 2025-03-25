from rest_framework import viewsets
from app.models import Product
from app.serializers import ProductSerializer
from app.views.admin_panel.product.product_list_view import ProductListView
from app.views.admin_panel.product.product_details_view import ProductDetailsView


''' This module contains the views for the admin panel. '''
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


__all__ = ['ProductViewSet', "ProductListView", "ProductDetailsView"]

        
            


    


