from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from app.models import Product




def products_list(request, category=None):
    # search for products in db
    # products = Product.objects.order_by("-rate")[:5]
    products = Product.objects.all()
    # give our data to the template
    template = loader.get_template("client/index.html")
    context = {"products": products}
    return HttpResponse(template.render(context, request))

def products_details(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    template = loader.get_template("client/product_details.html")
    context = {"product": product}
    return HttpResponse(template.render(context, request))


# # Клиентская страница
# def home(request):
#     return render(request, 'client/home.html')

# # Административная панель
# @login_required
# def dashboard(request):
#     return render(request, 'admin_panel/dashboard.html')


