from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from app.models import Product
from app.forms import ProductForm
from django.views import View
from app.serializers import ProductSerializer
from django.views.generic import ListView


class ProductListView(ListView):
    '''View for displaying a list of products'''

    model = Product
    template_name = "admin_panel/index.html"
    context_object_name = "products"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":  # Если форма для добавления товара отправлена
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()  # Сохраняем новый товар
                return redirect('admin_products_list')  # Перенаправляем на страницу списка товаров
            
        return self.get(request, *args, **kwargs)  # Для отображения списка товаров и формы
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()  # Передаем объект товара в шаблон
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product was added successfully!")
        return super().form_valid(form)
