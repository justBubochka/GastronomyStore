from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse
from django.template import loader
from django.views import View
from django.contrib import messages
from app.models import Product
from app.forms import ProductForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class ProductDetailsView(UpdateView):
    '''View for displaying the details of a product'''

    model = Product
    form_class = ProductForm
    template_name = "admin_panel/product_details.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object  # Передаем объект товара в шаблон
        return context

    def post(self, request, *args, **kwargs):
        # Если отправили форму на удаление, удаляем товар
        if 'delete' in request.POST:
            product = get_object_or_404(Product, pk=self.kwargs['pk'])
            product.delete()
            return redirect('admin_products_list')  # Перенаправление на список товаров (или на другую страницу)

        # Обработка обычной формы обновления
        return super().post(request, *args, **kwargs)


    def get_success_url(self):
        # Передаем pk объекта после успешного обновления
        return reverse_lazy('admin_product_details', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, "Product was changed successfully!")
        return super().form_valid(form)

    # def get(self, request, pk):
    #     try:    
    #         product = get_object_or_404(Product, pk=pk)
    #     except Http404:
    #         return HttpResponse("Product not found")
        
    #     template = loader.get_template("admin_panel/product_details.html")
    #     form = ProductForm(instance=product)
    #     context = {"product": product, 'form': form}

    #     return HttpResponse(template.render(context, request))
    
    # def post(self, request, pk):
    #     try:    
    #         product = get_object_or_404(Product, pk=pk)
    #     except Http404:
    #         return HttpResponse("Product not found")
        
    #     if request.method == "POST":
    #         if request.POST.get('delete'):
    #             product.delete()
    #             return redirect('admin_products_list')
    #         elif request.POST.get('edit'):
    #             form = ProductForm(request.POST, request.FILES, instance=product)
    #             context = {"product": product, 'form': form}

    #             if form.is_valid():
    #                 form.save()
    #                 messages.success(request, "Product was changed successfully!")
    #                 return redirect('admin_products_list')
    #             return render(request, 'admin_panel/product_details.html', context)
            

