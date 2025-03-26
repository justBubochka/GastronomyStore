from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from app.models import Product, Category
from django.views import View
from app.forms import ProductForm
from django.contrib import messages


@method_decorator(staff_member_required, name="dispatch")
class AdminHomeView(View):
    '''Home page view'''

    def get(self, request):

        return render(request, "admin_panel/index.html")
    

@method_decorator(staff_member_required, name="dispatch")
class ProductListView(View):
    '''View for displaying a list of products'''

    def get(self, request):
        products = Product.objects.all()
        template = loader.get_template("admin_panel/products.html")
        form = ProductForm()
        context = {"products": products, 'form': form }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Product added successfully!")
                return redirect('admin_products_list')
            
        # if not valid then return the form with errors
        products = Product.objects.all()
        return render(request, 'admin_panel/products.html', {'products': products, 'form': form})

@method_decorator(staff_member_required, name="dispatch")
class ProductDetailsView(View):
    '''View for displaying the details of a product'''

    def get(self, request, pk):
        try:    
            product = get_object_or_404(Product, pk=pk)
        except Http404:
            return HttpResponse("Product not found")
        
        template = loader.get_template("admin_panel/product_details.html")
        form = ProductForm(instance=product)
        context = {"product": product, 'form': form}

        return HttpResponse(template.render(context, request))
    
    def post(self, request, pk):
        try:    
            product = get_object_or_404(Product, pk=pk)
        except Http404:
            return HttpResponse("Product not found")
        
        if request.method == "POST":
            if request.POST.get('delete'):
                product.delete()
                return redirect('admin_products_list')
            elif request.POST.get('edit'):
                form = ProductForm(request.POST, request.FILES, instance=product)
                context = {"product": product, 'form': form}

                if form.is_valid():
                    form.save()
                    messages.success(request, "Product was changed successfully!")
                    return redirect('admin_products_list')
                return render(request, 'admin_panel/product_details.html', context)
        
            


    


