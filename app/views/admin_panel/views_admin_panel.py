from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from app.models import Product, Category
from django.views import View
from app.forms import ProductForm
from django.contrib import messages



class ProductListView(View):
    '''View for displaying a list of products'''

    def get(self, request):
        products = Product.objects.all()
        template = loader.get_template("admin_panel/index.html")
        form = ProductForm()
        context = {"products": products, 'form': form }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Product added successfully!")
                return redirect('admin_products_list')
            
        # if not valid then return the form with errors
        products = Product.objects.all()
        return render(request, 'admin_panel/index.html', {'products': products, 'form': form})


class ProductDetailsView(View):
    '''View for displaying the details of a product'''

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        template = loader.get_template("admin_panel/product_details.html")
        form = ProductForm(instance=product)
        context = {"product": product, 'form': form}

        return HttpResponse(template.render(context, request))
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.method == "POST":
            if request.POST.get('delete'):
                product.delete()
                return redirect('admin_products_list')
            elif request.POST.get('edit'):
                form = ProductForm(request.POST, instance=product)
                context = {"product": product, 'form': form}

                if form.is_valid():
                    form.save()
                    messages.success(request, "Product was changed successfully!")
                    return redirect('admin_products_list')
                return render(request, 'admin_panel/product_details.html', context)
            


    


