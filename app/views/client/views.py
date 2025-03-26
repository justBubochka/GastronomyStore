from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from app.models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.forms import LoginForm


def login_view(request):
    '''View for user login'''

    if request.method == "POST":
        # get the user data
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  #  the same as username = request.POST.get("username")
            password = form.cleaned_data["password"]
            # authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser or user.is_staff:
                    return redirect("admin_products_list")
                return redirect("client_home")
            else:
                return render(request, "login.html", {"error": "Invalid credentials"})
    elif request.user.is_authenticated:
        return redirect("client_home")
    
    return render(request, "login.html")

def registration_view(request):
    if request.method == "POST":
        # get the user data
        username = request.POST.get("username")
        password = request.POST.get("password")
        # create a new user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("login")
    return render(request, "registration.html")

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def client_home(request, category=None):
    return render(request, "client/index.html", {"user": request.user})
    


def products_list(request, category=None):
    # search for products in db
    # products = Product.objects.order_by("-rate")[:5]
    products = Product.objects.all()
    # give our data to the template
    template = loader.get_template("client/products.html")
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


