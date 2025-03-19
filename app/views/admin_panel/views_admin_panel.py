from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.admin.views.decorators import staff_member_required
from app.models import Product, Category



@staff_member_required
def products_list_admin(request, category=None):
    # search for products in db
    # products = Product.objects.order_by("-rate")[:5]
    products = Product.objects.all()
    # give our data to the template
    template = loader.get_template("admin_panel/index.html")
    context = {"products": products}
    return HttpResponse(template.render(context, request))

@staff_member_required
def product_details_admin(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    template = loader.get_template("admin_panel/product_details.html")
    context = {"product": product}
    return HttpResponse(template.render(context, request))


