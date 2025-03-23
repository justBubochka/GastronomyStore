"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app.views.client import views
from app.views.admin_panel import views_admin_panel

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls'))
    path("admin/", admin.site.urls),

    # 📌 Клиентская часть
    path('', views.products_list, name='client_products_list'),
    path('product/<int:product_id>/', views.products_details, name='client_product_details'),

    # 📌 Админская часть
    path('admin_panel/', views_admin_panel.ProductListView.as_view(), name='admin_products_list'),
    path('admin_panel/product/<int:pk>/', views_admin_panel.ProductDetailsView.as_view(), name='admin_product_details')
]
