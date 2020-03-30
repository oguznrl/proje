from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from django.contrib import messages
cart_item = 0
cart_list = list()

def home(request):
    return render(request, "home.html", {"cart_item": get_cart_item()})


def explore(request):
    products = Product.objects.all()
    args = {"products": products,
            "all_categories": get_all_categories(products), "cart_item": get_cart_item()
            }
    return render(request, "explore.html", args)


def get_all_categories(products):
    categories = list()
    i = 0
    for product in products:
        for i in range(len(product.categories.split(','))):
            categories.append(product.categories.split(',')[i])
    return list(dict.fromkeys(categories))


def your_cart(request):
    return render(request, "your_cart.html")


def product_buy_detail(request, product, id):
    product = get_object_or_404(Product, id=id)
    args = {"product": product}
    return render(request, "product_buy_detail.html", args)


def buy_product(request,product,id):
    obje=get_object_or_404(Product,id=id)
    obje.count-=1
    obje.save()
    return redirect('/explore')

def add_cart(request,id):
    cart_list = get_cart_list()
    product = get_object_or_404(Product, id=id)
    product.cart_count += 1
    product.save()
    set_cart_item(get_cart_item() + 1)
    if not product in cart_list:
        cart_list.append(product)
    messages.success(
        request, "Başarıyla '{}' Ürününü Sepete Eklediniz.".format(product.name))
    return redirect("/explore")

def get_cart_list():
    global cart_list
    return cart_list


def get_cart_item():
    global cart_item
    return cart_item


def set_cart_item(item):
    global cart_item
    cart_item = item
    return cart_item

    

    

    