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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls'))
    path("admin/", admin.site.urls),

    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.logout_view, name='logout'),

    # 📌 Клиентская часть
    path('', views.client_home, name='client_home'),
    path('products', views.products_list, name='client_products_list'),
    path('product/<int:product_id>/', views.products_details, name='client_product_details'),

    # 📌 Админская часть
    path('admin_panel/', views_admin_panel.AdminHomeView.as_view(), name='admin_home'),
    path('admin_panel/products', views_admin_panel.ProductListView.as_view(), name='admin_products_list'),
    path('admin_panel/product/<int:pk>/', views_admin_panel.ProductDetailsView.as_view(), name='admin_product_details')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)